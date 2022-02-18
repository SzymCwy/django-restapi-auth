from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class Role(models.TextChoices):
        STANDARD = 'US', _('User')
        PREMIUM = 'PR', _('Premium')
        MODERATOR = 'MR', _('Moderator')
        ADMIN = 'AD', _('Admin')
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.STANDARD)
    birth = models.DateField(help_text='format : YYYY-MM-DD', null=True, blank=True)
    lastmodified = models.DateField(auto_now=True)
    profilelink = models.SlugField()

    def __str__(self):
        return f'{self.lastmodified, self.username}'
