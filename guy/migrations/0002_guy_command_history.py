# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0001_initial'),
        ('guy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guy',
            name='command_history',
            field=models.ForeignKey(to='command.Command', null=True),
            preserve_default=True,
        ),
    ]
