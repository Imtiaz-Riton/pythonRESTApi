# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20210621_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeltodelete',
            name='name',
            field=models.CharField(default='ModelToDelete', max_length=50),
        ),
        migrations.AddField(
            model_name='snippet',
            name='name',
            field=models.CharField(default='Snippet', max_length=50),
        ),
    ]
