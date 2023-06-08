from django.urls import path

from .views import Marks, SensorReadings

urlpatterns = [
    path('marks/', Marks.as_view()),
    path('sensor-readings/<int:id>/', SensorReadings.as_view()),
]