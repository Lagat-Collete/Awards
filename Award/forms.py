from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


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


class RegisterUserForm(UserCreationForm):
  email = forms.EmailField(label='Email')

  class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
   class Meta:
    model =

class EditProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('profile_photo','bio','user')