from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError(
            'Senha fraca. Sua senha deve ter: no mínimo 8 caracteres, '
            'uma letra maiúscula e uma letra minúscula.'
        )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'password': 'Senha',
        }
        error_messages = {
            'username': {
                'required': 'Este campo é obrigatório'
            },
            'email': {
                'required': 'Este campo é obrigatório'
            },
            'password': {
                'required': 'Este campo é obrigatório'
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Seu nome de usuário'
            }),
            'password': forms.PasswordInput(),
        }

    email = forms.EmailField(
        required=True,
        label='E-mail',
        error_messages={
            'required': 'Este campo é obrigatório'
        },
    )

    password = forms.CharField(
        required=True,
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Sua senha'
        }),
        validators=[strong_password],
        error_messages={
            'required': 'Este campo é obrigatório'
        },
    )

    confirm_password = forms.CharField(
        required=True,
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repita a senha'
        }),
        error_messages={
            'required': 'Este campo é obrigatório'
        },
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'As senhas não coincidem')

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return email

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('Este e-mail já está em uso')

        return email