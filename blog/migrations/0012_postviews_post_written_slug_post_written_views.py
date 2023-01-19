# Generated by Django 4.1.4 on 2022-12-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_written_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPAdress', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='post_written',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='post_written',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='game_views', to='blog.postviews'),
        ),
    ]