# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0002_systemuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemuser',
            name='user',
        ),
    ]
