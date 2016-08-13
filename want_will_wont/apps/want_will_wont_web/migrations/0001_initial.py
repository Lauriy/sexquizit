# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('paid_only', models.BooleanField(verbose_name='paid only', default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySpecification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('activity', models.ForeignKey(verbose_name='activity', to='want_will_wont_web.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('owner_token', models.UUIDField(default=uuid.uuid4, verbose_name='owner token')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSetAccessToken',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('token', models.UUIDField(default=uuid.uuid4, verbose_name='token')),
                ('answer_set', models.ForeignKey(verbose_name='answer set', to='want_will_wont_web.AnswerSet')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'female'), (1, 'male')], blank=True, null=True)),
                ('user', models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answerset',
            name='profile',
            field=models.ForeignKey(null=True, verbose_name='profile', to='want_will_wont_web.Profile', blank=True),
        ),
    ]
