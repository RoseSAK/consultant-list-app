# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=150)),
                ('email', models.EmailField(default=b'', max_length=254, blank=True)),
                ('status', models.CharField(max_length=20, choices=[(b'A', b'Administrator'), (b'M', b'Manager'), (b'U', b'Standard User')])),
                ('user', models.OneToOneField(default=b'NullUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
