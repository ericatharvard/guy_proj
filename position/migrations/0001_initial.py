# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('orientation', models.PositiveIntegerField(default=0, choices=[(0, b'North'), (1, b'East'), (2, b'South'), (3, b'West')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
