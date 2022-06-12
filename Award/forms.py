from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = '__all__'

class ProfileForm(forms.ModelForm):
  class meta:
    model = Profile
    fields = '__all__'

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']