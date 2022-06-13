from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
  path('search/', views.search_results, name='search_results'),
  path('',views.project, name='homepage'),
  path('api/profile/', views.ProfileList.as_view()),
  path('api/project/', views.ProjectList.as_view()),
  path('userprofile/<username>', views.user_profile, name='user_profile'),
  path('profile/<username>', views.profile, name='profile'),
  path('project/<project>', views.project_rating, name='project'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)