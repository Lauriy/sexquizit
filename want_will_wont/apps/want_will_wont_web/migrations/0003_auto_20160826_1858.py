# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0002_auto_20160826_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'activities'},
        ),
        migrations.AlterModelOptions(
            name='activitycategory',
            options={'verbose_name_plural': 'activity categories'},
        ),
        migrations.AddField(
            model_name='activity',
            name='description_en',
            field=models.CharField(verbose_name='description', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='description_et',
            field=models.CharField(verbose_name='description', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='description_en',
            field=models.CharField(verbose_name='description', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='description_et',
            field=models.CharField(verbose_name='description', max_length=255, null=True),
        ),
    ]
