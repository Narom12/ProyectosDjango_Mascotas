# Generated by Django 4.0.5 on 2022-06-17 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_tipouser_alter_usuario_tipo_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tipoUser',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_user',
            field=models.CharField(max_length=30, verbose_name='Tipo usuario'),
        ),
    ]
