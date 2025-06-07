from django.contrib import admin
from .models import Reservation, Menu

admin.site.register(Reservation)  # Import your models here
# Register your models here.

admin.site.register(Menu)  # Register the Reservation model with the admin site