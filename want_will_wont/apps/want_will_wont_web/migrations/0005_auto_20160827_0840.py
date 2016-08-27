# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0004_auto_20160826_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('value', models.PositiveSmallIntegerField(choices=[(0, 'want'), (1, 'will'), (2, "won't")])),
            ],
        ),
        migrations.RemoveField(
            model_name='answerset',
            name='answers',
        ),
        migrations.AddField(
            model_name='activity',
            name='paired_with',
            field=models.ForeignKey(to='want_will_wont_web.Activity', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='paired_with',
            field=models.ForeignKey(to='want_will_wont_web.ActivityCategory', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='activity',
            field=models.ForeignKey(to='want_will_wont_web.Activity'),
        ),
        migrations.AddField(
            model_name='answer',
            name='profile',
            field=models.ForeignKey(to='want_will_wont_web.Profile', verbose_name='profile', null=True, blank=True),
        ),
    ]
