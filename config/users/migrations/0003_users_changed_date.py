# Generated by Django 3.2 on 2023-02-18 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230217_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='changed_date',
            field=models.DateTimeField(null=True),
        ),
    ]
