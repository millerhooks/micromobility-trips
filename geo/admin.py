from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from django.conf import settings
from . import models
from leaflet.admin import LeafletGeoAdmin
from mapbox_location_field.spatial.admin import SpatialMapAdmin
from django.core.management import call_command

class TrafficIncidentAdmin(SpatialMapAdmin):
    search_fields = ['traffic_report_id', 'publish_date', 'address', 'issue_reported']
    list_display = ['traffic_report_id', 'publish_date', 'address', 'issue_reported']

class StateAdmin(LeafletGeoAdmin):
    search_fields = ['name']
    list_display = ['name', 'density']

__custom_admins__ = {
    'TrafficIncident': TrafficIncidentAdmin,
    'AustinHex': LeafletGeoAdmin,
    'State': StateAdmin,
}

for model in models.__admin__:
    params = [getattr(models, model)]
    if model in __custom_admins__:
        params.append(__custom_admins__[model])
    else:
        _dyn_class = type('%sAdmin' % ( str(model),), (geoadmin.OSMGeoAdmin,), {})
        #( VersionAdmin, ), {} )
        params.append(_dyn_class)
    admin.site.register(*params)