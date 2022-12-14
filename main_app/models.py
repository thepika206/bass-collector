from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Amp(models.Model):
  manufacturer = models.CharField(max_length=100)
  model_name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.manufacturer + ' ' + self.model_name 

  def get_absolute_url(self):
    return reverse('amps_detail', kwargs={'amp_id': self.id})
    
class Bass(models.Model):
  manufacturer = models.CharField(max_length=100)
  model_name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  amps = models.ManyToManyField(Amp)

  class Meta:  
    verbose_name_plural = 'Basses'

  def __str__(self):
    return self.manufacturer + ' ' + self.model_name

  def get_absolute_url(self):
    return reverse('basses_detail', kwargs={'bass_id': self.id})


class Musician(models.Model):
  name = models.CharField(max_length=100)
  bass = models.ForeignKey(Bass, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

# class Rig(models.Model):
#   name = models.CharField(max_length=100)
#   bass = models.ForeignKey(Bass, on_delete=models.CASCADE)
#   amps = models.ForeignKey(Amp, on_delete=models.CASCADE)
  
#   def __str__(self):
#     return self.name

#   def get_absolute_url(self):
#     return reverse('rigs_index')

# ! need to make migrations