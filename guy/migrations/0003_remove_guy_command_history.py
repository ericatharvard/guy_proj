# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0002_guy_command_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guy',
            name='command_history',
        ),
    ]
