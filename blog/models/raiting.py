from django.db import models
from blog.models import posts


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "RaitingStar"
        verbose_name_plural = "RaitingStars"

class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    post = models.ForeignKey(posts.Post_written, on_delete=models.CASCADE, verbose_name="post")

    def __str__(self):
        return f"{self.star} - {self.post}"
    
    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
