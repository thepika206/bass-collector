from django.db import models
from django.urls import reverse

# Create your models here.
class Bass(models.Model):
  manufacturer = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.model

  def get_absolute_url(self):
    return reverse('basses_detail', kwargs={'bass_id': self.id})