# Generated by Django 3.0.4 on 2020-03-20 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200317_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 17, 29, 28, 994081)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 17, 29, 28, 994081)),
        ),
    ]
