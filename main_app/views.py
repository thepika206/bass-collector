from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Bass

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