from django.views.generic import ListView, DetailView
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        # Only display active courses to students
        return Course.objects.filter(is_active=True).order_by('-created_at')

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'