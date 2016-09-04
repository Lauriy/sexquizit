# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0008_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 4, 18, 10, 42, 931770, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 4, 18, 10, 45, 327426, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 4, 18, 10, 49, 548526, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitycategory',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 4, 18, 10, 51, 525650, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 4, 18, 10, 53, 725227, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 4, 18, 10, 55, 813185, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerset',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 4, 18, 10, 57, 589307, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerset',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 4, 18, 10, 59, 173471, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 4, 18, 11, 0, 702197, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 4, 18, 11, 2, 388160, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 4, 18, 11, 3, 965609, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 9, 4, 18, 11, 5, 996538, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
