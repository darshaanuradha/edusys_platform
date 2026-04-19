from django.urls import path
from . import views

app_name = 'courses' # Namespace for clean reverse URLs

urlpatterns = [
    path('', views.CourseListView.as_view(), name='list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
]