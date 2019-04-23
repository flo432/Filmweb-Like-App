# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=250)),
                ('for_movie', models.ForeignKey(default=b'', to='Movies.Movie')),
                ('user', models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
