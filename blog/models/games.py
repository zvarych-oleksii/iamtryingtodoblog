import datetime

from django.db import models
from django.utils.text import slugify

from blog.models import SubCategory
from django.contrib.auth.models import User

from users.models import Profile


class GameViews(models.Model):
    IPAddres= models.CharField(max_length=100)
    def __str__(self):
        return self.IPAddres

class Game(models.Model):
    title_of_game = models.CharField(max_length=40, default="Doom", blank=False, verbose_name="Game title:")
    gameplay_text = models.TextField(max_length=3000, default="Fine", blank=False, verbose_name="Gameplay description:")
    conclusion_text = models.TextField(max_length=3000, default="Fine game", blank=False, verbose_name="Conclusion:")
    image_of_game = models.ImageField(blank=False)
    price = models.SmallIntegerField(blank=False, help_text="max 5", default=0, verbose_name="Price rating:")
    graphics = models.SmallIntegerField(blank=False, help_text='max 5', default=0, verbose_name="Graphics rating:")
    levels = models.SmallIntegerField(blank=False, help_text="max 5", default=0, verbose_name='Levels rating:')
    dificulty = models.SmallIntegerField(blank=False, help_text="max 5", default=0, verbose_name="Dificulty rating:")
    category = models.ManyToManyField(SubCategory, blank=False, verbose_name="Category:")
    created = models.DateField(default=datetime.date.today, blank=False, verbose_name='Created:', help_text="Don't touch it!")
    slug = models.SlugField(blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    all_list = models.Manager()
    views = models.ManyToManyField(GameViews, related_name="game_views", blank=True)
    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        ordering = ["title_of_game"]
    def __str__(self):
        return self.title_of_game

    def save(self, *args, **kwargs):
        value = self.title_of_game
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    @staticmethod
    def get_games_by_id(ids):
        return Game.all_list.filter(id_in=ids)
