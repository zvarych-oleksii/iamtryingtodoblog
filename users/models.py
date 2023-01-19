from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE, null=True)
    name = models.CharField(blank=False, max_length=50, unique=False, default="steve")
    avatar = models.ImageField("Avatar", upload_to="profiles/", default='default/default_avatar.png', null=True, blank=True)
    first_name = models.CharField("First Name", max_length=50, blank=False)
    last_name = models.CharField("Last Name", max_length=50, blank=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("Profile-detail", kwargs={"pk":self.pk})
    def get_initial_date(self):
        initial_data = {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        return initial_data

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""