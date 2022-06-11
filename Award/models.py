
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
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
  profile_photo = CloudinaryField('photo')
  bio = models.TextField(max_length=200, default="My Bio")
  email = models.EmailField()

  def save_profile(self):
        self.save()

  def delete_profile(self):
      self.delete()

  def __str__(self):
    return str(self.user)

class Project(models.Model):
  title = models.CharField(max_length=50)
  image = CloudinaryField('image')
  description = models.TextField()
  developer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='project')
  hyperlink = models.URLField()
  day_posted = models.DateTimeField(auto_now_add=True)
  

  def save_project(self):
        self.save()

  def delete_project(self):
      self.delete()

  def __str__(self):
    return str(self.user)

  @classmethod
  def search_by_title(cls,search_term):
    project = cls.objects.filter(title__icontains=search_term)
    return project

class Rating(models.Model):
  design = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
  usability = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
  content = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

  def __str__(self):
      return str(self.pk)

