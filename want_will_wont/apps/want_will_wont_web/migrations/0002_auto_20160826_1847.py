# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
        ),
        migrations.RemoveField(
            model_name='activityspecification',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='answersetaccesstoken',
            name='answer_set',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='paid_only',
        ),
        migrations.RemoveField(
            model_name='answerset',
            name='owner_token',
        ),
        migrations.AddField(
            model_name='activity',
            name='shown_for_gender',
            field=models.PositiveSmallIntegerField(choices=[(0, 'female'), (1, 'male')], default=0, verbose_name='shown for gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerset',
            name='answers',
            field=jsonfield.fields.JSONField(default={}, verbose_name='answers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answerset',
            name='secret',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='secret'),
        ),
        migrations.DeleteModel(
            name='ActivitySpecification',
        ),
        migrations.DeleteModel(
            name='AnswerSetAccessToken',
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(verbose_name='category', blank=True, null=True, related_name='activities', to='want_will_wont_web.ActivityCategory'),
        ),
    ]
