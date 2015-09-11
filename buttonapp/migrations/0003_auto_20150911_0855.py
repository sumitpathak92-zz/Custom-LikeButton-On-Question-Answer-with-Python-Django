# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buttonapp', '0002_question_was_published_recently'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='was_published_recently',
            field=models.BooleanField(verbose_name=b'True'),
        ),
    ]
