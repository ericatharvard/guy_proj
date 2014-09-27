# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0002_auto_20140923_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='y',
            field=models.IntegerField(default=0),
        ),
    ]
