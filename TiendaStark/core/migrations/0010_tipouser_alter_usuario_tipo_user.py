# Generated by Django 4.0.5 on 2022-06-17 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_manbod_categoria_bod_alter_manbod_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUser',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=80, verbose_name=' Tipo de usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoria'),
        ),
    ]
