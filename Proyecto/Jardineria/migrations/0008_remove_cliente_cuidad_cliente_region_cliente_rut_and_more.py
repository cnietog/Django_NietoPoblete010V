# Generated by Django 4.0.4 on 2022-06-12 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jardineria', '0007_alter_producto_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cuidad',
        ),
        migrations.AddField(
            model_name='cliente',
            name='region',
            field=models.CharField(default='Some String', max_length=40, verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(default='Some String', max_length=40, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='perfil',
            field=models.ImageField(blank=True, null=True, upload_to='Cliente'),
        ),
    ]