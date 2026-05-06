from django import forms
from django.core.exceptions import ValidationError
from ..models import Marmita


class MarmitaForm(forms.ModelForm):
    class Meta:
        model = Marmita

        fields = [
            'nome',
            'descricao',
            'ingredientes',
            'peso',
            'preco',
            'imagem',
        ]

        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'ingredientes': 'Ingredientes',
            'peso': 'Peso (g)',
            'preco': 'Preço (R$)',
            'imagem': 'Imagem',
        }

        help_texts = {
            'nome': 'Nome da marmita',
            'descricao': 'Descreva o produto',
            'ingredientes': 'Separe por vírgula ou linha',
            'peso': 'Peso em gramas',
            'preco': 'Ex: 19.90',
        }

        error_messages = {
            'nome': {
                'required': 'Esse campo é obrigatório'
            },

            'descricao': {
                'required': 'Esse campo é obrigatório'
            },

            'ingredientes': {
                'required': 'Esse campo é obrigatório'
            },

            'peso': {
                'required': 'Informe o peso'
            },

            'preco': {
                'required': 'Informe o preço'
            },
        }

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Ex: Marmita Fitness'
            }),

            'descricao': forms.Textarea(attrs={
                'placeholder': 'Descrição da marmita'
            }),

            'ingredientes': forms.Textarea(attrs={
                'placeholder': 'Arroz, frango, legumes...'
            }),

            'peso': forms.NumberInput(attrs={
                'placeholder': '500',
                'min': '1'
            }),

            'preco': forms.NumberInput(attrs={
                'placeholder': '19.90',
                'step': '0.01',
                'min': '0.01'
            }),
            
            'imagem': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')

        if not nome:
            return nome

        nome = nome.strip()

        if len(nome) < 3:
            raise ValidationError(
                'O nome precisa ter pelo menos 3 caracteres'
            )

        if len(nome) > 160:
            raise ValidationError(
                'O nome ultrapassou o limite permitido'
            )

        return nome

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')

        if not descricao:
            return descricao

        descricao = descricao.strip()

        if len(descricao) < 10:
            raise ValidationError(
                'A descrição precisa ter pelo menos 10 caracteres'
            )

        if len(descricao) > 360:
            raise ValidationError(
                'A descrição ultrapassou o limite permitido'
            )

        return descricao

    def clean_ingredientes(self):
        ingredientes = self.cleaned_data.get('ingredientes')

        if not ingredientes:
            return ingredientes

        ingredientes = ingredientes.strip()

        if len(ingredientes) < 5:
            raise ValidationError(
                'Informe ingredientes válidos'
            )

        if len(ingredientes) > 360:
            raise ValidationError(
                'Os ingredientes ultrapassaram o limite permitido'
            )

        return ingredientes

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')

        if peso <= 0:
            raise ValidationError(
                'O peso deve ser maior que zero'
            )

        if peso > 10000:
            raise ValidationError(
                'Peso muito alto'
            )

        return peso

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')

        if preco <= 0:
            raise ValidationError(
                'O preço deve ser maior que zero'
            )

        return preco