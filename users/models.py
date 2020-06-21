from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class MyUser (AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, null=False, max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str_(self):
        return self.email



class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have e-mail address.')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staf = True
        user.save(using=self._db)

        return user

        objects = MyUserManager()

        def __str__(self):
            return self.email
