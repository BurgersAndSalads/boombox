from django.shortcuts import render, redirect
from .models import Playlist, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

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


def home(request):
    return render(request, 'base.html')

def myplaylist(request):
    return render(request, 'myplaylist.html')

def details(request):
    return render(request, 'details.html', {'playlist': Playlist, 'songs': Song})

songlist = [ {'name':'first song'}, {'name':'second song'}, {'name':'third song'}]
def landing(request):
    return render(request, 'landing.html', {'user': {'name':'yiren'}, 'songs': songlist})

def login(request):
    return render(request, 'login.html')
