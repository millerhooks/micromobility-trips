from django.contrib.gis.db import models
from mapbox_location_field.spatial.models import SpatialLocationField  
from django.utils.text import slugify
import requests
 

__admin__ = ['AustinHex', 'TrafficIncident', 'State', 'WeatherAPI']

class WeatherAPI(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    @property
    def data(self):
        resp = requests.get(self.url)
        return resp.text.strip('/n')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(WeatherAPI, self).save(*args, **kwargs)

class TrafficIncident(models.Model):
    ISSUE_REPORTED_CHOICES = [
        ("ZV", "zSTALLED VEHICLE"),
        ("TH", "Traffic Hazard"),
        ("CU", "Crash Urgent"),
        ("CS", "Crash Service"),
        ("CO", "COLLISION"),
        ("TD", "TRFC HAZD/ DEBRIS"),
        ("TI", "Traffic Impediment"),
        ("CW", "COLLISION WITH INJURY"),
        ("LL", "LOOSE LIVESTOCK"),
        ("CL", "COLLISN/ LVNG SCN"),
        ("SV", "Stalled Vehicle"),
        ("CP", "COLLISION/PRIVATE PROPERTY"),
        ("VH", "VEHICLE FIRE"),
        ("BD", "BLOCKED DRIV/ HWY"),
        ("BA", "BOAT ACCIDENT"),
        ("TF", "TRAFFIC FATALITY"),
        ("AP", "AUTO/ PED"),
        ("IR", "ICY ROADWAY"),
        ("FA", "FLEET ACC/ INJURY"),
        ("NH", "N / HZRD TRFC VIOL"),
        ("OH", "OBSTRUCT HWY"),
        ("CF", "COLLISN / FTSRA"),
        ("HW", "HIGH WATER"),
        ("FF", "FLEET ACC/ FATAL"),
    ]
    traffic_report_id = models.CharField(max_length=100, blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    issue_reported = models.CharField(
        max_length=2, 
        choices=ISSUE_REPORTED_CHOICES, 
        blank=True, 
        null=True)
    location = SpatialLocationField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    status_date = models.DateTimeField(blank=True, null=True)
    
    def get_choice(self, string):
        return {v: k for k, v in self.ISSUE_REPORTED_CHOICES}[string]

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.traffic_report_id, self.publish_date, self.address, self.get_issue_reported_display())

class AustinHex(models.Model):
    number = models.IntegerField()
    hex = models.PolygonField()

    def __str__(self):
        return str(self.number)

class State(models.Model):
    name = models.CharField(max_length=100)
    density = models.DecimalField(max_digits=8, decimal_places=4)
    shape = models.PolygonField()

    def __str__(self):
        return self.name
