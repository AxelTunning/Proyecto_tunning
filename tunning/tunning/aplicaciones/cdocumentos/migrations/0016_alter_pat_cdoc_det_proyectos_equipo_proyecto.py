# Generated by Django 4.2.4 on 2023-08-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdocumentos', '0015_alter_pat_cdoc_det_proyectos_codigoproyecto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pat_cdoc_det_proyectos',
            name='equipo_proyecto',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
