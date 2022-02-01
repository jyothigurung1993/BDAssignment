"""from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

from ..electronicsapp.models import TimestampedModel


class User(AbstractUser, TimestampedModel):
    full_name = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=100)
    last_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return "{0}#{1}".format(self.full_name, self.id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)"""

