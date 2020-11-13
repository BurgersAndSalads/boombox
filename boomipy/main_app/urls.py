from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  # user log in
  path('login/', views.login, name='login'),
  #  landing page
  path('landing/', views.landing, name='landing'),
  # user playlists
  path('myplaylist/', views.myplaylist, name='myplaylist'),
  #  playlist details
  path('details/', views.details, name='details'),
]

