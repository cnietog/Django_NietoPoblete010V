# Generated by Django 4.0.4 on 2022-06-12 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jardineria', '0009_alter_cliente_region_alter_cliente_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='comentario',
            field=models.CharField(max_length=140, verbose_name='Comentario'),
        ),
    ]
