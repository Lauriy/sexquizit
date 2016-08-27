# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('want_will_wont_web', '0005_auto_20160827_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_set',
            field=models.ForeignKey(to='want_will_wont_web.AnswerSet', related_name='answers', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='want_will_wont_web.ActivityCategory', related_name='activities'),
        ),
    ]
