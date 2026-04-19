from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages
from .models import Enrollment
from courses.models import Course

class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    template_name = 'enrollments/enrollment_form.html'
    fields = [] # No form fields needed; we extract data from the URL and logged-in user
    success_url = reverse_lazy('courses:list')

    def get_context_data(self, **kwargs):
        # Pass the specific course to the template so we can display its title
        context = super().get_context_data(**kwargs)
        context['course'] = get_object_or_404(Course, id=self.kwargs['course_id'])
        return context

    def form_valid(self, form):
        course = get_object_or_404(Course, id=self.kwargs['course_id'])
        user = self.request.user

        # Prevent duplicate enrollments
        if Enrollment.objects.filter(student=user, course=course).exists():
            messages.warning(self.request, f"You are already enrolled in {course.title}.")
            return redirect('courses:list')

        # Atomic transaction for capacity management
        with transaction.atomic():
            locked_course = Course.objects.select_for_update().get(id=course.id)
            current_enrollments = Enrollment.objects.filter(course=locked_course, status='active').count()
            
            if current_enrollments >= locked_course.capacity:
                messages.error(self.request, "Sorry, this course is currently at maximum capacity.")
                return redirect('courses:detail', pk=course.id)

            # Save the enrollment
            form.instance.student = user
            form.instance.course = locked_course
            messages.success(self.request, f"Successfully enrolled in {locked_course.title}!")
            return super().form_valid(form)