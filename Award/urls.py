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
  path('',views.home_page, name='homepage'),
  path('search/', views.search_results, name='search_results')
]