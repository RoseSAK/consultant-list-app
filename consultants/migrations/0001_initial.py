# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=200, null=True, blank=True)),
                ('practice', models.CharField(blank=True, max_length=2, null=True, choices=[(b'TC', b'Technology Consulting'), (b'SE', b'Software Engineering'), (b'D', b'Delivery'), (b'C', b'Consulting')])),
                ('role', models.CharField(max_length=200, null=True, blank=True)),
                ('teams', models.CharField(max_length=200, null=True, blank=True)),
                ('skills', models.CharField(max_length=200, null=True, blank=True)),
                ('sectors', models.CharField(max_length=200, null=True, blank=True)),
                ('notes', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
    ]
