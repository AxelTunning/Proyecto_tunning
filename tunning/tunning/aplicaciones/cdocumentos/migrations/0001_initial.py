# Generated by Django 4.2.4 on 2023-08-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pat_cdo_parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta_temporal', models.CharField(max_length=300)),
                ('ruta_defitiva', models.CharField(max_length=300)),
            ],
        ),
    ]
