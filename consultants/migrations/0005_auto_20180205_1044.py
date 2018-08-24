# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0004_auto_20180205_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='practice',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'TC', b'Technology Consulting'), (b'SE', b'Software Engineering'), (b'D', b'Delivery'), (b'C', b'Corporate')]),
        ),
    ]
