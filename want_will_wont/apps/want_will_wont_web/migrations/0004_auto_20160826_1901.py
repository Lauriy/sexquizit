# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0003_auto_20160826_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='shown_for_gender',
            field=models.PositiveSmallIntegerField(verbose_name='shown for gender', default=2, choices=[(0, 'female'), (1, 'male'), (2, 'both')]),
        ),
    ]
