# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0003_remove_guy_command_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guy',
            name='position',
            field=models.OneToOneField(null=True, default=None, blank=True, to='position.Position'),
        ),
    ]
