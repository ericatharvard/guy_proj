# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0004_command_guy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='command',
            old_name='name',
            new_name='action',
        ),
    ]
