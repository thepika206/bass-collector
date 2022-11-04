from django.db import models

# Create your models here.
class Bass(models.Model):
  manufacturer = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  description = models.CharField(max_length=250)

  def __str__(self):
    return self.model