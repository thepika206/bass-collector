from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('basses/', views.basses_index, name='basses_index'),
  path('about/', views.about, name='about'),
]