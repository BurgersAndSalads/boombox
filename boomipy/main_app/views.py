from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import UserCreationForm
from .models import Playlist, Song


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

# dummy data
songlist = [ {'name':'MORE', 'link': 'https://www.youtube.com/watch?v=3VTkBuxU4yk'}, {'name':'avengers', 'link':'https://www.youtube.com/watch?v=FOabQZHT4qY'}, {'name':'third song'}]
def landing(request):
  return render(request, 'landing.html', {'username': {'name':'yiren'}, 'songs': songlist})

def login(request):
  return render(request, 'home.html')
