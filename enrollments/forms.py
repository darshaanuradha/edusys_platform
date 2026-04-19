from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course'] # The student is injected automatically by the view