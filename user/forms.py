from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, EmailField, PasswordInput

from user.models import CustomUser


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['id'] = 'username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
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
                'placeholder': 'Senha'
            },
        ),
        required=True
    )
