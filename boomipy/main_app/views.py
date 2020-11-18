from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import UserCreationForm
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


# this class will be used when we have a functioning model 
# class MyPlaylist(ListView):
#     Playlist = Playlist.objects.filter(user=user)
#     model = Playlist
# will be used for when we have the login installed
# @login_required


def myplaylist(request):
  # playlist = Playlist.objects.filter(user=request.user)
  playlist = Playlist.objects.all()
  username = request.user
  return render(request, 'myplaylist.html', {'playlist': playlist})

def details(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  return render(request, 'details.html', {'playlist': playlist, "id": playlist_id})

# CRUD for playlist
class PlaylistCreate(CreateView):
  model = Playlist
  fields = ['name', 'description']
  success_url = '/myplaylist/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PlaylistUpdate(UpdateView):
  model = Playlist
  fields = ['name', 'description', 'songs']

class PlaylistDelete(DeleteView):
  model = Playlist
  success_url = '/myplaylist/'

def landing(request):
  username = request.user
  playlist = Playlist.objects.all()
  return render(request, 'landing.html', {'username': {'name': username}, 'songs': playlist})

def login(request):
  return render(request, 'home.html')




# def SongCreate(request, playlist_id):
#   return render(request, 'main_app/song_form.html', {'playlist_id': playlist_id})

def SongCreate(request, playlist_id):
  template = 'main_app/song_form.html'
  form = SongForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect(f'myplaylist/{playlist_id}')
  
  context = {"form": form}
  return render(request, template, context)

def SongAssociate(request, playlist_id, song_id):
  Playlist.objects.get(id=playlist_id).songs.add(song_id)
  return redirect(f'/myplaylist/{playlist_id}')

class SongDelete(DeleteView):
  model = Song
  success_url = '/myplaylist/'

