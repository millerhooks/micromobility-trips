# Generated by Django 3.1.13 on 2021-08-19 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0008_weatherapi'),
        ('users', '0002_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='weather_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.weatherapi'),
        ),
    ]
