# Generated by Django 4.1.4 on 2022-12-24 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_avatar'),
        ('blog', '0013_remove_post_written_views_delete_postviews_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='post_written',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Author'),
        ),
    ]