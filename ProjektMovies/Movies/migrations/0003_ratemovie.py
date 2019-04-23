# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Movies', '0002_commentmovie'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('for_movie', models.ForeignKey(default=b'', to='Movies.Movie')),
                ('user', models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
