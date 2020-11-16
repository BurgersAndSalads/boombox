from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Song(models.Model):
    artist = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

# making a change so git can detect change to merge to master