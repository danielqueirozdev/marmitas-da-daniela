from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError('''
            Weak password: Your password must include:
            - 8 or more characters
            - At least one lowercase letter
            - At least one uppercase letter
        ''')
    

class RegisterForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'E-mail',
            'password': 'Password',
        }
        help_texts = {
            'first_name': 'Put your first name',
            'last_name': 'Put your last name',
            'username': 'Put your username',
            'email': 'Put your e-mail',
            'password': 'Put your password',
        }
        error_messages = {
            'first_name': {
                'required': 'This field must not be empty'
            },
            'last_name': {
                'required': 'This field must not be empty'
            },
            'username': {
                'required': 'This field must not be empty'
            },
            'email': {
                'required': 'This field must not be empty'
            },
            'password': {
                'required': 'This field must not be empty'
            },
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username here'
            }),
            'password': forms.PasswordInput(),
        }

    first_name = forms.CharField(
        required=True,
    )

    last_name = forms.CharField(
        required=True,
    )

    email = forms.EmailField(
        required=True,
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[strong_password]
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password here'
        }),
        help_text=('Type your password again')
    )

    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Your two passwords must be the same')

        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return email

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('This email is already in use')

        return email