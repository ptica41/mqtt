from django.db import models


class Point(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.CharField(max_length=10, null=True)
    longitude = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.latitude[:7]}:{self.longitude[:7]}"

    class Meta:
        db_table = 'point'


class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=50,  null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.unit}"

    class Meta:
        db_table = 'sensor'


class Indication(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    value = models.FloatField()
    status = models.CharField(max_length=15, null=True, blank=True)
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start} | {self.point} | {self.sensor} - {self.value}"

    class Meta:
        db_table = 'indication'

