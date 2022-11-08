from django.urls import path
from . import views

urlpatterns = [
  #? path('[http url]', views.[where in the views file], name='[reference this route from templates]' )
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  #! localhost:8000/basses
  path('basses/', views.basses_index, name='basses_index'),
  path('basses/<int:bass_id>/', views.basses_detail, name='basses_detail'),
  
  # class based view to create basses via form
  path('basses/create/', views.BassCreate.as_view(), name='basses_create'),

  path('basses/<int:pk>/update/', views.BassUpdate.as_view(), name='basses_update'),
  
  path('basses/<int:pk>/delete/', views.BassDelete.as_view(), name='basses_delete'),
  # localhost:8000/basses/int:bass_id/add_musician
  path('basses/<int:bass_id>/add_musician/', views.add_musician, name='add_musician'),


  #! /amps
  path('amps/', views.amps_index, name='amps_index'),
  
  path('amps/create/', views.AmpCreate.as_view(), name='amps_create'),
  
  path('amps/<int:amp_id>/', views.amps_detail, name='amps_detail'),
  
  path('amps/<int:pk>/update/', views.AmpUpdate.as_view(), name='amps_update'),

  path('amps/<int:pk>/delete/', views.AmpDelete.as_view(), name='amps_delete'),

  # ! comma after each route!
]