# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_publication_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date_order',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
