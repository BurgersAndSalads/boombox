from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  # user log in
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  #  landing page
  path('landing/', views.landing, name='landing'),
  # user playlists
  path('myplaylist/', views.myplaylist, name='myplaylist'),
  #  playlist details
  path('playlist/<int:playlist_id>', views.details, name='playlist_details'),
]
