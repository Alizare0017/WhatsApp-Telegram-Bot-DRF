# Generated by Django 3.2 on 2023-03-04 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='changed_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]