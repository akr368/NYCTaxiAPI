# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VendorID', models.TextField()),
                ('tpep_pickup_datetime', models.TextField()),
                ('tpep_dropoff_datetime', models.TextField()),
                ('passenger_count', models.TextField()),
                ('trip_distance', models.TextField()),
                ('pickup_longitude', models.TextField()),
                ('pickup_latitude', models.TextField()),
                ('RatecodeID', models.TextField()),
                ('store_and_fwd_flag', models.TextField()),
                ('dropoff_longitude', models.TextField()),
                ('dropoff_latitude', models.TextField()),
                ('payment_type', models.TextField()),
                ('fare_amount', models.TextField()),
                ('extra', models.TextField()),
                ('mta_tax', models.TextField()),
                ('tip_amount', models.TextField()),
                ('tolls_amount', models.TextField()),
                ('improvement_surcharge', models.TextField()),
                ('total_amount', models.TextField()),
            ],
        ),
    ]