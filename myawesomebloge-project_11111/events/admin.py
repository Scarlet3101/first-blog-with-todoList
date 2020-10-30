from django.contrib import admin

# Register your models here.
from .models import Event

admin.site.site_header = "Anews Admin Page"
admin.site.register(Event)
