# Generated by Django 4.0.5 on 2022-06-17 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_manproducto_categoria_man'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manbod',
            name='categoria_bod',
            field=models.CharField(max_length=30, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='manbod',
            name='id',
            field=models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]