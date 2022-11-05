from django.urls import path
from . import views

urlpatterns = [
  #? path('[http url]', views.[where in the views file], name='[reference this route from templates]' )
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('basses/', views.basses_index, name='basses_index'),
  path('basses/<int:bass_id>/', views.basses_detail, name='basses_detail'),
  # class based view to create basses via form
  path('basses/create/', views.BassCreate.as_view(), name='basses_create'),
  # ! comma after each route!
]