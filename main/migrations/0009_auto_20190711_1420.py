# Generated by Django 2.1.5 on 2019-07-11 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190711_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 11, 14, 20, 42, 260993), verbose_name='date published'),
        ),
    ]
