# Generated by Django 3.2 on 2023-03-04 09:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20230304_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='changed_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 9, 10, 57, 189228, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='exp_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 9, 10, 57, 189228, tzinfo=utc)),
        ),
    ]
