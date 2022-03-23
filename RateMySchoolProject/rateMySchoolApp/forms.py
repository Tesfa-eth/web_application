from django import forms
from .models import Universities

# connect the form to the model... this file is not used for now.
class UniversitySearch(forms.ModelForm):
    class Meta:
        model = Universities
        fields = ['name']