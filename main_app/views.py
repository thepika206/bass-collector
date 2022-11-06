from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Bass
from .models import Amp


# home view
def home(request):
  return render(request, 'home.html')


# about view
def about(request):
  return render(request, 'about.html')

# basses list view
def basses_index(request):
  basses = Bass.objects.all()
  return render(request, 'basses/index.html', {'basses':basses})

# bass details view
def basses_detail(request, bass_id):
  bass = Bass.objects.get(id=bass_id)
  return render(request, 'basses/detail.html', {'bass':bass})

# add bass form... Class Based hence the (CreateView) argument that was imported above
class BassCreate(CreateView):
  model = Bass
  fields = '__all__'
  #? alternatively:  fields = ['manufacturer', 'model', 'description']

class BassUpdate(UpdateView):
  model = Bass
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['manufacturer', 'model_name', 'description']

class BassDelete(DeleteView):
  model = Bass
  success_url = '/basses/'

# amps list view
def amps_index(request):
  amps = Amp.objects.all()
  return render(request, 'amps/index.html', {'amps': amps})

class AmpCreate(CreateView):
  model = Amp
  fields = '__all__'

def amps_detail(request, amp_id):
  amp = Amp.objects.get(id=amp_id)
  return render(request, 'amps/detail.html', {'amp':amp})
  