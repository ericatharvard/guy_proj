# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0006_auto_20140923_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guy',
            name='position',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='position.Position'),
        ),
    ]
