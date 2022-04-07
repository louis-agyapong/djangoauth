from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("email address"), unique=True)
    username = models.CharField(_("Username"), max_length=256, blank=True)
    first_name = models.CharField(_("first name"), max_length=256)
    last_name = models.CharField(_("last name"), max_length=256)
    middle_name = models.CharField(_("middle name"), max_length=256, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("Date joined"), default=timezone.now, editable=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        if self.middle_name:
            return ("%s %s %s" % (self.first_name, self.middle_name, self.last_name)).strip()
        return self.email

    def short_name(self) -> str:
        return f"{self.last_name.lower()}_{self.first_name.lower()}"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)
