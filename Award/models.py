
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from django.dispatch import receiver
import datetime as dt
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from urllib.parse import urlparse


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

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
        if created:
         Profile.objects.create(user=instance)

  @receiver(post_save, sender = User)
  def save_user_profile(sender, instance, **kwargs):
       instance.profile.save()

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
    return str(self.developer)

  @classmethod
  def search_by_title(cls,search_term):
    project = cls.objects.filter(title__icontains=search_term)
    return project

class Rating(models.Model):
    rating = (
        (1, '1'), (2, '2'),(3, '3'),(4, '4'),(5, '5'), (6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),
    )
    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings
    
    def __str__(self):
        return f'{self.project} Rating'