# Generated by Django 3.2 on 2023-02-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20230218_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='exp_date',
            field=models.DateTimeField(null=True),
        ),
    ]