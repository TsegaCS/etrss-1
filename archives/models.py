from django.db import models
from datetime import datetime
from mapapp.models import latlng

class Archives(models.Model):
    # user_id = models.IntegerField(blank=True)
    latitude=models.FloatField()
    longitude=models.FloatField()
    place_name = models.CharField(max_length=255, blank=True, null=True)
    request_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    
    applicationField = models.CharField(max_length=255, blank=True)
    orderType = models.CharField(max_length=255, blank=True)
    productLevel = models.CharField(max_length=255, blank=True)
    delivery_media = models.CharField(max_length=255, blank=True)
    # surface = models.CharField(max_length=255, blank=True)
    kmlKmz = models.FileField(blank=True, null=True)
    shapeFile = models.FileField(blank=True, null=True)
    data_format = models.CharField(max_length=100, blank=True)
    satellite_source = models.CharField(max_length=255, blank=True)
    cloud_cover = models.CharField(max_length=100, blank=True)
    nto_additional_descriptions = models.CharField(max_length=100, blank=True)
    aoi_additional_descriptions = models.CharField(max_length=100, blank=True)
    confirmation_email = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "archive"
        verbose_name_plural = "archives"


    def __str__(self):
        return self.place_name