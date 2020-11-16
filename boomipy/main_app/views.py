from django.shortcuts import render

from django.views.generic import ListView

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
      login(request, user)
      return redirect('accounts/login.html')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'base.html')


# this class will be used when we have a functioning model 
# class MyPlaylist(ListView):
#     Playlist = Playlist.objects.filter(user=user)
#     model = Playlist
# will be used for when we have the login installed
# @login_required

def myplaylist(request):
    # playlist = Playlist.objects.filter(user=request.user)
    playlist = Playlist.objects.all()
    return render(request, '/playlist.html', {'playlist': playlist})

def myplaylist(request):
    return render(request, 'myplaylist.html')
def details(request):
    return render(request, 'details.html')
def landing(request):
    return render(request, 'landing.html')
def login(request):
    return render(request, 'login.html')
