# Generated by Django 4.2.4 on 2023-08-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdocumentos', '0010_listado_personal_delete_vistaoffice365'),
    ]

    operations = [
        migrations.AddField(
            model_name='pat_cdoc_header_proyectos',
            name='Total_documento',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pat_cdoc_header_proyectos',
            name='transmittal_ing',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pat_cdoc_header_proyectos',
            name='transmittal_ot',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
