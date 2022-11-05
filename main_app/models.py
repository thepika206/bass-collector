from django.db import models
from django.urls import reverse

# Create your models here.
class Bass(models.Model):
  manufacturer = models.CharField(max_length=100)
  model_name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.model

  def get_absolute_url(self):
    return reverse('basses_detail', kwargs={'bass_id': self.id})

class Amp(models.Model):
  manufacturer = models.CharField(max_length=100)
  model_name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.model

  def get_absolute_url(self):
    return reverse('amps_detail', kwargs={'amp_id': self.id})

# ! need to make migrations