# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0007_auto_20140923_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guy',
            name='position',
            field=models.OneToOneField(null=True, blank=True, to='position.Position'),
        ),
    ]
