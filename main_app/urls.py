from django.urls import path
from . import views

urlpatterns = [
  #? path('[http url]', views.[where in the views file], name='[reference this route from templates]' )
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  #! bass views
  path('basses/', views.basses_index, name='basses_index'),
  path('basses/<int:bass_id>/', views.basses_detail, name='basses_detail'),
  
  # class based view to create basses via form
  path('basses/create/', views.BassCreate.as_view(), name='basses_create'),

  path('basses/<int:pk>/update/', views.BassUpdate.as_view(), name='basses_update'),
  
  path('basses/<int:pk>/delete/', views.BassDelete.as_view(), name='basses_delete'),

  #! amp views
  path('amps/', views.amps_index, name='amps_index'),
  path('amps/create/', views.AmpCreate.as_view(), name='amps_create'),
  path('amps/<int:amp_id>/', views.amps_detail, name='amps_detail'),
  # ! comma after each route!
]