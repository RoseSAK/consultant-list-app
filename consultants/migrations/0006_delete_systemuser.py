# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0005_auto_20180205_1044'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SystemUser',
        ),
    ]
