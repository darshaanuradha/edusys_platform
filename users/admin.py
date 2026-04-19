# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Display these fields in the admin list view
    list_display = ('username', 'email', 'is_student', 'is_instructor', 'is_staff')
    
    # Add custom fields to the user editing screen in the admin panel
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('is_student', 'is_instructor')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)