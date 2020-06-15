# Generated by Django 3.0.4 on 2020-06-01 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('place_name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_taken', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('applicationField', models.CharField(blank=True, max_length=255)),
                ('orderType', models.CharField(blank=True, max_length=255)),
                ('productLevel', models.CharField(blank=True, max_length=255)),
                ('delivery_media', models.CharField(blank=True, max_length=255)),
                ('kmlKmz', models.FileField(blank=True, null=True, upload_to='')),
                ('shapeFile', models.FileField(blank=True, null=True, upload_to='')),
                ('data_format', models.CharField(blank=True, max_length=100)),
                ('satellite_source', models.CharField(blank=True, max_length=255)),
                ('cloud_cover', models.CharField(blank=True, max_length=100)),
                ('nto_additional_descriptions', models.CharField(blank=True, max_length=100)),
                ('aoi_additional_descriptions', models.CharField(blank=True, max_length=100)),
                ('confirmation_email', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]