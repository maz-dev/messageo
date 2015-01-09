# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField(max_length=1024)),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
