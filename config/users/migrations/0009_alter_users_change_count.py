# Generated by Django 3.2 on 2023-02-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_users_exp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='change_count',
            field=models.IntegerField(default=0),
        ),
    ]