from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    # Pass the course_id through the URL so the view knows what the user is enrolling in
    path('enroll/<int:course_id>/', views.EnrollmentCreateView.as_view(), name='enroll'),
]