# Generated by Django 4.0.5 on 2022-06-15 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categoriaproducto_manproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_user', models.CharField(max_length=30, verbose_name='Tipo usuario')),
                ('rut', models.CharField(max_length=13, verbose_name='RUT')),
                ('nombres', models.CharField(max_length=60, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Tipo usuario')),
                ('direccion', models.CharField(max_length=60, verbose_name='Dirección')),
                ('suscripcion', models.BooleanField(max_length=1, verbose_name='Con suscripción')),
                ('imagen', models.ImageField(default='cristian_gomez.jpg', upload_to='img/', verbose_name='Imagen')),
            ],
        ),
    ]
