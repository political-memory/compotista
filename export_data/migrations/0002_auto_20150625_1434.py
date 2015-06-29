# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('export_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exportedrevision',
            name='data',
        ),
        migrations.AddField(
            model_name='exportedrevision',
            name='path',
            field=models.FilePathField(default=''),
            preserve_default=False,
        ),
    ]
