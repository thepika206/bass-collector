from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# home view
def home(request):
  return HttpResponse('<h1>hello bass</h1>')

# about view
def about(request):
  return render(request, 'about.html')
  # return HttpResponse('<h1>About the bass collector</h1>')