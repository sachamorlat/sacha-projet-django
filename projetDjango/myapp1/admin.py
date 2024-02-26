from django.contrib import admin
from .models import Voyage, Reservation, Itineraire

# Register your models here.
admin.site.register(Voyage) 
admin.site.register(Reservation) 
admin.site.register(Itineraire) 