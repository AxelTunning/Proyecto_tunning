# Generated by Django 4.2.4 on 2023-08-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdocumentos', '0002_proyectos_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pat_cdo_header_proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoProyecto', models.CharField(blank=True, max_length=10, null=True)),
                ('dia_entrega_doc', models.IntegerField(choices=[(7, '7 dias'), (10, '10 dias'), (12, '12 dias'), (15, '15 dias'), (20, '20 dias')], default=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
