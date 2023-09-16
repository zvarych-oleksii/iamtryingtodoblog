import datetime
from django.db import models
from django.utils.text import slugify
from blog.models import categories
from users.models import Profile


class Post_written(models.Model):
    title = models.CharField(max_length=40, blank=False, verbose_name="Name of post")
    content = models.TextField(blank=False, verbose_name="Content of post", default="Ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis ipsum labore suspendisse ultrices gravida....")
    category = models.ManyToManyField(categories.Category, blank=False)
    image = models.ImageField(blank=True)
    date = models.DateField(default=datetime.date.today)
    slug = models.SlugField(blank=True)
    all_posts = models.Manager()
    views = models.IntegerField(default=0, blank=False)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE, verbose_name="Author", null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['title']
    
    @staticmethod
    def get_post_by_id(ids):
        return Post_written.all_posts.filter(id_in=ids)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
