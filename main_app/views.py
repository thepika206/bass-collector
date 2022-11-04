from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

class Bass:
  def __init__(self, manufacturer, model, strings, image):
    self.manufacturer = manufacturer
    self.model = model
    self.strings = strings
    self.image = image

basses = [
  Bass('Fender', 'Precision', 4, 'fender-precision-200.png'),
  Bass('Fender', 'Jazz', 4, 'fender-jazz-200.png'),
  Bass('Musicman', 'Stingray 5', 5, 'eb-stingray5-200.png'),
  Bass('Warwick', 'FNA Jazzman', 5, 'warwick-fna-200.png'),
  Bass('Gibson', 'The Ripper', 4, 'gibson-ripper-200.png'),
]



# home view
def home(request):
  return HttpResponse('<h1>hello bass</h1>')

# about view
def about(request):
  return render(request, 'about.html')

# basses view
def basses_index(request):
  return render(request, 'basses/index.html', {'basses':basses})