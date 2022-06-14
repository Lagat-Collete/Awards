from django.test import TestCase
from .models import *
# Create your tests here.

class ProfileTestClass(TestCase):

  #set up method
  def setUp(self):
      self.user = User(id=1, username='lagat',password='12345lagat')
      self.user.save()

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()


class ProjectTestClass(TestCase):
  def setUp(self):
    self.user =User.objects.create(id=1, username='lagat')
    self.project = Project.objects.create(id=1, title='testing', image='image.jng',description='description test',developer='lagat',hyperlink='http://ur.com')
    

  def test_save_project(self):
    self.project.save_project()
    project = Project.objects.all()
    self.assertTrue(len(project)>0)
    
  def test_search_project(self):
    self.project.save()
    project = Project.search_project('test')
    self.assertTrue(len(project)>0)

  def test_delete_project(self):
      self.project.delete_project()
      project = Project.search_project('test')
      self.assertTrue(len(project) < 1)

class TestRating(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='prime')
        self.post = Post.objects.create(id=1, title='testing post', photo='testphoto.png', description='Test post description',
                                        user=self.user, url='http://ur.coml')
        self.rating = Rating.objects.create(id=1, design=8, usability=7, content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)
