from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, EmailField, PasswordInput
from django.utils.translation import gettext_lazy as _

from user.models import CustomUser


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['id'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = _('Email')
        self.fields['email'].widget.attrs['aria-describedby'] = 'emailHelp'

        self.fields['password'].widget.attrs['id'] = 'password'

    email = EmailField(
        required=True,
    )

    password = CharField(
        label=CustomUser._meta.get_field('password').verbose_name,
        widget=PasswordInput(
            attrs={
                'class': 'form-control form-control-user',
                'placeholder': _('Password')
            },
        ),
        required=True
    )
