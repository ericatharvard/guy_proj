# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0003_auto_20140923_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('position', models.OneToOneField(to='position.Position')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
