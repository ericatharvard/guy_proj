# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='orientation',
            new_name='dir',
        ),
    ]
