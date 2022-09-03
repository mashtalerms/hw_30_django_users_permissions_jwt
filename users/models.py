from django.contrib.auth.models import AbstractUser
from django.db import models

from ads.models.location import Location


class User(AbstractUser):

    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE = [(MEMBER, MEMBER), (MODERATOR, MODERATOR), (ADMIN, ADMIN)]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(choices=ROLE, max_length=9)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username
