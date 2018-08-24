# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0006_delete_systemuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='practice',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
