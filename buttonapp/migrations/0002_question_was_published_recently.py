# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buttonapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='was_published_recently',
            field=models.BooleanField(default=datetime.datetime(2015, 9, 11, 8, 55, 24, 313165, tzinfo=utc), verbose_name=False),
            preserve_default=False,
        ),
    ]
