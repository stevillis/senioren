from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """CustomUser Model"""

    name = models.CharField(
        verbose_name='Nome',
        max_length=80,
        null=False,
        blank=False
    )

    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        null=False,
        blank=False
    )

    is_staff = models.BooleanField(
        verbose_name='Membro da equipe',
        default=False,
        help_text='Indica que usuário consegue acessar este site de administração.'
    )

    is_active = models.BooleanField(
        verbose_name='Ativo',
        default=True,
        help_text='Indica que o usuário será tratado como ativo. Ao invés de excluir contas de usuário, desmarque isso.',
    )

    date_joined = models.DateTimeField(
        verbose_name='Data de registro',
        default=timezone.now
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    def __str__(self):  # pylint: disable=invalid-str-returned
        return self.email

    class Meta:
        """Metadata options"""
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
