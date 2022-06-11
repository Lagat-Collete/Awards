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