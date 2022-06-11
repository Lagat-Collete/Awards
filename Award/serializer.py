from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('id','user','bio','profile_photo','email')

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model =Project
    fields =('id','title','image','description','developer','hyperlink','day_posted')