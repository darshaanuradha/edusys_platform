# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields here
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    
    # Best practice: Add related_name to avoid clashes if you ever use auth.User
    # You can also add things like 'bio' or 'profile_picture' later.
    
    def __str__(self):
        return self.username