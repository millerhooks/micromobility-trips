# Generated by Django 3.1.13 on 2021-08-19 11:35

from django.db import migrations, models
import mapbox_location_field.spatial.models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0004_auto_20210819_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficincident',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trafficincident',
            name='issue_reported',
            field=models.CharField(blank=True, choices=[('ZV', 'zSTALLED VEHICLE'), ('TH', 'Traffic Hazard'), ('CU', 'Crash Urgent'), ('CS', 'Crash Service'), ('CO', 'COLLISION'), ('TD', 'TRFC HAZD/ DEBRIS'), ('TI', 'Traffic Impediment'), ('CW', 'COLLISION WITH INJURY'), ('LL', 'LOOSE LIVESTOCK'), ('CL', 'COLLISN/ LVNG SCN'), ('SV', 'Stalled Vehicle'), ('CP', 'COLLISION/PRIVATE PROPERTY'), ('VH', 'VEHICLE FIRE'), ('BD', 'BLOCKED DRIV/ HWY'), ('BA', 'BOAT ACCIDENT'), ('TF', 'TRAFFIC FATALITY'), ('AP', 'AUTO/ PED'), ('IR', 'ICY ROADWAY'), ('FA', 'FLEET ACC/ INJURY'), ('NH', 'N / HZRD TRFC VIOL'), ('OH', 'OBSTRUCT HWY'), ('CF', 'COLLISN / FTSRA'), ('HW', 'HIGH WATER'), ('FF', 'FLEET ACC/ FATAL')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='trafficincident',
            name='location',
            field=mapbox_location_field.spatial.models.SpatialLocationField(blank=True, map_attrs={}, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='trafficincident',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trafficincident',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trafficincident',
            name='status_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trafficincident',
            name='traffic_report_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]