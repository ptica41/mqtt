from django.contrib import admin
from .models import Sensor, Indication, Point

admin.site.register(Sensor)
admin.site.register(Indication)
admin.site.register(Point)
