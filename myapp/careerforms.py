from django import forms
from .careermodels import CareerApplication

class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = ['name', 'phone', 'email', 'position', 'resume']
