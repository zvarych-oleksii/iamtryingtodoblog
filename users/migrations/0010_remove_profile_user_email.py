# Generated by Django 4.1.4 on 2023-01-17 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_name_alter_profile_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_email',
        ),
    ]
