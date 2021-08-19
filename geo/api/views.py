from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter

from geo.models import AustinHex, TrafficIncident, State
from .serializers import AustinHexSerializer, TrafficIncidentSerializer, StateSerializer

'''
class RegionFilter(GeoFilterSet):
    contains_geom = GeometryFilter(name='geom', lookup_expr='contains')

    class Meta:
        model = TrafficIncident
        filterset_fields = []

class GeojsonLocationList(generics.ListCreateAPIView):
    # -- other omitted view attributes --- #
    pagination_class = GeoJsonPagination
'''

class AustinHexList(viewsets.ModelViewSet):
    queryset = AustinHex.objects.all()
    serializer_class = AustinHexSerializer
    bbox_filter_field = 'hex'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional

class TrafficIncidentList(viewsets.ModelViewSet):
    queryset = TrafficIncident.objects.all()
    serializer_class = TrafficIncidentSerializer
    bbox_filter_field = 'location'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional

class StateList(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    bbox_filter_field = 'shape'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True # Optional