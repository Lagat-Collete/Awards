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
  path('home_page/',views.home_page, name='homepage'),
  path('search/', views.search_results, name='search_results'),
  path('',views.project, name='project'),
  path('api/profile/', views.ProfileList.as_view()),
  path('api/project/', views.ProjectList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)