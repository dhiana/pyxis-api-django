# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Runs',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('skips', models.IntegerField(null=True, blank=True)),
                ('fails', models.IntegerField(null=True, blank=True)),
                ('passes', models.IntegerField(null=True, blank=True)),
                ('run_time', models.FloatField(null=True, blank=True)),
                ('artifacts', models.TextField(null=True, blank=True)),
                ('run_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'managed': 'False',
                'db_table': 'runs',
            },
        ),
    ]
