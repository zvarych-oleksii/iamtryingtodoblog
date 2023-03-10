# Generated by Django 4.1.4 on 2023-02-07 22:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name of category:')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
            managers=[
                ('all_categories', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='GameViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPAddres', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post_written',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Name of post')),
                ('content', models.TextField(default='Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum labore suspendisse ultrices gravida....', verbose_name='Content of post')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateField(default=datetime.date.today)),
                ('slug', models.SlugField(blank=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Author')),
                ('category', models.ManyToManyField(to='blog.category')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['title'],
            },
            managers=[
                ('all_posts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'RaitingStar',
                'verbose_name_plural': 'RaitingStars',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name of subcategory:')),
            ],
            managers=[
                ('all_subcategories', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('text', models.TextField(max_length=1500, verbose_name='message')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.reviews', verbose_name='parent')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post_written', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post_written', verbose_name='post')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ratingstar', verbose_name='star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_game', models.CharField(default='Doom', max_length=40, verbose_name='Game title:')),
                ('gameplay_text', models.TextField(default='Fine', max_length=3000, verbose_name='Gameplay description:')),
                ('conclusion_text', models.TextField(default='Fine game', max_length=3000, verbose_name='Conclusion:')),
                ('image_of_game', models.ImageField(upload_to='')),
                ('price', models.SmallIntegerField(default=0, help_text='max 5', verbose_name='Price rating:')),
                ('graphics', models.SmallIntegerField(default=0, help_text='max 5', verbose_name='Graphics rating:')),
                ('levels', models.SmallIntegerField(default=0, help_text='max 5', verbose_name='Levels rating:')),
                ('dificulty', models.SmallIntegerField(default=0, help_text='max 5', verbose_name='Dificulty rating:')),
                ('created', models.DateField(default=datetime.date.today, help_text="Don't touch it!", verbose_name='Created:')),
                ('slug', models.SlugField(blank=True)),
                ('category', models.ManyToManyField(to='blog.subcategory', verbose_name='Category:')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('views', models.ManyToManyField(blank=True, related_name='game_views', to='blog.gameviews')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
                'ordering': ['title_of_game'],
            },
            managers=[
                ('all_list', django.db.models.manager.Manager()),
            ],
        ),
    ]
