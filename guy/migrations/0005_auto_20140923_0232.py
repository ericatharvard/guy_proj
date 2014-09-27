# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0004_auto_20140923_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guy',
            name='position',
            field=models.ForeignKey(to='position.Position'),
        ),
    ]
