# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('org_title', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField()),
                ('duration', models.DurationField(blank=True)),
                ('relase_date', models.DateField()),
                ('poster', models.URLField(blank=True)),
                ('trailer', models.URLField(blank=True)),
            ],
        ),
    ]
