# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StationInfo(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    indexnum = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    station_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'station_info'

class Weather(models.Model):
    type = models.CharField(max_length=45,blank=False, null=False )
    temperature = models.IntegerField(blank=True,null=False)
    dew_point = models.IntegerField(blank=True,null=False)
    humidity = models.IntegerField(blank=True,null=True)
    wind_speed = models.IntegerField(blank=True,null=True)
    wind_gust = models.IntegerField(blank=True,null=True)
    pressure = models.DecimalField(max_digits= 4, decimal_places=2,blank=True,null=True)
    precipitation = models.DecimalField(max_digits=2,decimal_places=1,blank=True,null=True)
    time = models.DateTimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'weather'


    