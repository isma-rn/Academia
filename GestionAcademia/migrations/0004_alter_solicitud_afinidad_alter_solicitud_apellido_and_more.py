# Generated by Django 5.0.6 on 2024-05-31 02:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademia', '0003_remove_estudiante_afinidad_remove_solicitud_estatus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='afinidad',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='identificacion',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
