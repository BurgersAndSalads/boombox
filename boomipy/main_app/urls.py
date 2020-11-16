from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.login, name='login'),
  # user log in
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  #  landing page
  path('landing/', views.landing, name='landing'),
  # user playlists
  path('myplaylist/', views.myplaylist, name='myplaylist'),
  #  playlist details
  path('details/', views.details, name='details'),
]
