from django.contrib import admin

from .models import Bass, Amp, Musician


# Register your models here.
admin.site.register(Bass)
admin.site.register(Amp)
admin.site.register(Musician)
