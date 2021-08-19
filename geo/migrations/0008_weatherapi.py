# Generated by Django 3.1.13 on 2021-08-19 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0007_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
