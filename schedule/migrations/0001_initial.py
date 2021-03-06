# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-12 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('venue', models.CharField(max_length=50)),
                ('venue_url', models.URLField()),
                ('start', models.TimeField()),
                ('duration', models.PositiveIntegerField(default=60, help_text='In minutes')),
                ('title', models.CharField(blank=True, help_text='Leave blank to create gaps in the schedule', max_length=200)),
                ('speaker', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ('day', 'start'),
            },
        ),
    ]
