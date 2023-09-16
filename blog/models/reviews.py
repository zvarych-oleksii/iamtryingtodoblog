from django.db import models
from blog.models import posts


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("name", max_length=100)
    text = models.TextField("message", max_length=1500)
    parent = models.ForeignKey(
        'self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True
    )
    post = models.ForeignKey(
        posts.Post_written, on_delete=models.CASCADE, verbose_name="Post"
                             )
    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
