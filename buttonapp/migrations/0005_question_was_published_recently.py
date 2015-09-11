# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('buttonapp', '0004_remove_question_was_published_recently'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='was_published_recently',
            field=models.BooleanField(default=datetime.datetime(2015, 9, 11, 9, 15, 35, 344326, tzinfo=utc), verbose_name=b'was published recently?'),
            preserve_default=False,
        ),
    ]
