# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0003_remove_systemuser_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultant',
            old_name='name',
            new_name='consultant_name',
        ),
        migrations.RenameField(
            model_name='systemuser',
            old_name='name',
            new_name='user_name',
        ),
    ]
