# Generated by Django 4.2.4 on 2023-08-07 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdocumentos', '0005_pat_cdoc_listado'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pat_cdo_det_proyectos',
            new_name='Pat_cdoc_det_proyectos',
        ),
        migrations.RenameModel(
            old_name='Pat_cdo_header_proyectos',
            new_name='Pat_cdoc_header_proyectos',
        ),
        migrations.RenameModel(
            old_name='Pat_cdo_parametros',
            new_name='Pat_cdoc_parametros',
        ),
    ]