# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0005_auto_20140923_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guy',
            name='position',
            field=models.OneToOneField(to='position.Position'),
        ),
    ]
