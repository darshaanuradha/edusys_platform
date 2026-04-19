from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title