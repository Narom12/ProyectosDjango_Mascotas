from django.db import models

# Create your models here.
class Post(models.Model):
    id_descuento = models.CharField(max_length=6)
    codigo_descuento = models.CharField(max_length=6)