# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default=b'None location added', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default=b'None description added'),
            preserve_default=True,
        ),
    ]
