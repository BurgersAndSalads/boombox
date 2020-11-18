from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Playlist, Song
from .forms import SongForm


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      dj_login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def myplaylist(request):
  # playlist = Playlist.objects.filter(user=request.user)
  playlist = Playlist.objects.all()
  username = request.user
  return render(request, 'myplaylist.html', {'playlist': playlist, 'username': username})

@login_required
def details(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  songs = Song.objects.all()
  return render(request, 'details.html', {'playlist': playlist, "id": playlist_id, 'songs': songs})

# CRUD for playlist
class PlaylistCreate(LoginRequiredMixin, CreateView):
  model = Playlist
  fields = ['name', 'description']
  success_url = '/myplaylist/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
  model = Playlist
  fields = ['name', 'description', 'songs']

class PlaylistDelete(LoginRequiredMixin, DeleteView):
  model = Playlist
  success_url = '/myplaylist/'

@login_required
def landing(request):
  username = request.user
  playlist = Playlist.objects.all()
  return render(request, 'landing.html', {'username': username, 'songs': playlist})

def login(request):
  return render(request, 'home.html')

# add an item(song) to the database
class SongCreate(LoginRequiredMixin, CreateView):
  model = Song
  fields = '__all__'
  success_url = '/myplaylist/'

# associate the song to a specific playlist
@login_required
def SongAssociate(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).songs.add(song_id)
  return redirect(f'/myplaylist/{playlist_id}')

# unassociate the song to a specific playlist
@login_required
def SongUnAssociate(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).songs.remove(song_id)
  return redirect(f'/myplaylist/{playlist_id}')
