# Generated by Django 3.2 on 2023-02-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='plan',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='sent',
            field=models.IntegerField(null=True),
        ),
    ]
