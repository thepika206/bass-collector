from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bass
from .models import Amp
from .forms import MusicianForm

# home view
def home(request):
  return render(request, 'home.html')


# about view
def about(request):
  return render(request, 'about.html')

#! bass views
@login_required
def basses_index(request):
  basses = Bass.objects.filter(user=request.user)
  return render(request, 'basses/index.html', {'basses':basses})

@login_required
def basses_detail(request, bass_id):
  bass = Bass.objects.get(id=bass_id)
  # Get the amps the bass doesn't have
  amps_bass_doesnt_have = Amp.objects.exclude( id__in = bass.amps.all().values_list('id')).filter(user=request.user)
  print(request.user)
  musician_form = MusicianForm()
  return render(request, 'basses/detail.html', {
    'bass':bass, 'musician_form': musician_form, 'amps': amps_bass_doesnt_have
  })

@login_required
def assoc_amp(request, bass_id, amp_id):
  Bass.objects.get(id=bass_id).amps.add(amp_id)
  return redirect('basses_detail', bass_id=bass_id)

@login_required
def add_musician(request, bass_id):
  form = MusicianForm(request.POST)
  if form.is_valid():
    new_musician = form.save(commit=False)
    new_musician.bass_id = bass_id
    new_musician.save()
  return redirect('basses_detail', bass_id=bass_id)         

class BassCreate(LoginRequiredMixin, CreateView):
  model = Bass
  fields = ['manufacturer', 'model_name', 'description']
  #? alternatively:  fields = ['manufacturer', 'model', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BassUpdate(LoginRequiredMixin, UpdateView):
  model = Bass
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['manufacturer', 'model_name', 'description']

class BassDelete(LoginRequiredMixin, DeleteView):
  model = Bass
  success_url = '/basses/'

#! amp views
@login_required
def amps_index(request):
  amps = Amp.objects.filter(user=request.user)
  return render(request, 'amps/index.html', {'amps': amps})

class AmpCreate(CreateView):
  model = Amp
  fields = ['manufacturer', 'model_name', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required
def amps_detail(request, amp_id):
  amp = Amp.objects.get(id=amp_id)
  return render(request, 'amps/detail.html', {'amp':amp})
  
class AmpUpdate(LoginRequiredMixin, UpdateView):
  model = Amp
  fields = ['manufacturer', 'model_name', 'description']

class AmpDelete(LoginRequiredMixin, DeleteView):
  model = Amp
  success_url = '/amps/'

class Home(LoginView):
  template_name = 'home.html'
  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('basses_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})