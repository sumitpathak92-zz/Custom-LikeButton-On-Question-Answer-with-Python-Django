# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buttonapp', '0003_auto_20150911_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='was_published_recently',
        ),
    ]
