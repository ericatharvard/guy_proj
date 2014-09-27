# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guy', '0003_remove_guy_command_history'),
        ('command', '0003_command_issued_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='guy',
            field=models.ForeignKey(to='guy.Guy', null=True),
            preserve_default=True,
        ),
    ]
