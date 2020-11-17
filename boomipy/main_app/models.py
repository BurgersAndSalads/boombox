from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Song(models.Model):
    artist = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

#adding a redirect url for a successful playlist creation
class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    def __str__(self):
        return self.name

