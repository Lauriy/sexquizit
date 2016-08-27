# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0006_auto_20160827_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='answerset',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='answerset',
            name='secret',
        ),
    ]
