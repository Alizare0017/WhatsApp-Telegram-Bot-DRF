# Generated by Django 3.2 on 2023-02-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_users_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user_id',
            new_name='userID',
        ),
    ]