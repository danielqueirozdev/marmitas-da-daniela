from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu nome de usuário'
        }),
        error_messages={
            'required': 'Este campo é obrigatório'
        },
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Sua senha'
        }),
        error_messages={
            'required': 'Este campo é obrigatório'
        },
    )