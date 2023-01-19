# Generated by Django 4.1.4 on 2022-12-22 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_category_managers_alter_game_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameviews',
            name='post',
        ),
        migrations.AddField(
            model_name='game',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='game_views', to='blog.gameviews'),
        ),
        migrations.AlterField(
            model_name='gameviews',
            name='IPAddres',
            field=models.CharField(max_length=100),
        ),
    ]