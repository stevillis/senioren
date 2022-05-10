from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """CustomUser Model"""
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=80,
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        unique=True,
        null=False,
        blank=False
    )
    is_staff = models.BooleanField(
        verbose_name=_('Staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        verbose_name=_('Active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.email

    class Meta:
        """Metadata options"""
        verbose_name = _('User')
        verbose_name_plural = _('Users')
