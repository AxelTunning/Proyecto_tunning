# Generated by Django 4.2.4 on 2023-08-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdocumentos', '0017_alter_pat_cdoc_det_proyectos_codigoproyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pat_cdoc_det_proyectos',
            name='CodigoProyecto',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pat_cdoc_det_proyectos',
            name='equipo_proyecto',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
