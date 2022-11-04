from django.shortcuts import render
from .models import Bass

# home view
def home(request):
  return render(request, 'home.html')


# about view
def about(request):
  return render(request, 'about.html')

# basses view
def basses_index(request):
  basses = Bass.objects.all()
  return render(request, 'basses/index.html', {'basses':basses})

def basses_detail(request, bass_id):
  bass = Bass.objects.get(id=bass_id)
  return render(request, 'basses/detail.html', {'bass':bass})