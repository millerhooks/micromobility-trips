from django.contrib.gis.geos import Point
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField

from geo.models import AustinHex, TrafficIncident, State

class StateSerializer(GeoFeatureModelSerializer):
    density = serializers.DecimalField(max_digits=8, decimal_places=4)

    class Meta:
        model = State
        geo_field = "shape"
        fields = ['id', 'name', 'density', 'shape']

class AustinHexSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = AustinHex
        geo_field = "hex"
        fields = ['id', 'number', 'hex']

class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)

class TrafficIncidentSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    issue_reported = ChoiceField(choices=TrafficIncident.ISSUE_REPORTED_CHOICES)

    class Meta:
        model = TrafficIncident
        geo_field = "location"

        # you can also explicitly declare which fields you want to include
        # as with a ModelSerializer.
        fields = ('id', 'traffic_report_id', 'publish_date', 'address', 'issue_reported')
