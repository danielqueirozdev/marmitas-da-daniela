from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
from PIL import Image

# Create your models here.
class Marmita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=160, null=False)
    ingredientes = models.TextField(max_length=360, null=False)
    descricao = models.TextField(max_length=360, null=False)
    peso = models.IntegerField(null=False)
    preco = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        )
    imagem = models.ImageField(
        upload_to='marmitas/imagens/',
        null=False,
    )

    def __str__(self):
        return self.nome
    
    @staticmethod
    def resize_image(image, new_width=800, new_heigth=500):
        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)

        new_image = image_pillow.resize((new_width, new_heigth), Image.LANCZOS)

        new_image.save(
            image_full_path,
            optimize=True,
            quality=70,
        )

    def save(self, *args, **kwargs):
        saved = super().save(*args, **kwargs)

        if self.imagem:
            try:
                self.resize_image(self.imagem, 800, 500)
            except FileNotFoundError:
                ...

        return saved