# Generated by Django 4.1.4 on 2022-12-23 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]