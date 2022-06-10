
from turtle import title
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from django.dispatch import receiver
import datetime as dt
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
  profile_photo = CloudinaryField('photo')
  bio = models.TextField()

  def save_profile(self):
        self.save()

  def delete_profile(self):
      self.delete()

  def __str__(self):
    return str(self.user)

class Projects(models.Model):
  title = models.CharField(max_length=50)
  image = CloudinaryField('image')
  description = models.TextField()
  developer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='project')
  hyperlink = models.URLField()
  day_posted = models.DateTimeField(auto_now_add=True)
  email = models.EmailField()

  def save_project(self):
        self.save()

  def delete_project(self):
      self.delete()

  def __str__(self):
    return str(self.user)
