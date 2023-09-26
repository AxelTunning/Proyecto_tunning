# Generated by Django 4.2.4 on 2023-08-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdocumentos', '0008_pat_cdoc_listado_fecha_entrega'),
    ]

    operations = [
        migrations.CreateModel(
            name='VistaOffice365',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ficha', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('carNom', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'PAV_Office365',
                'managed': False,
            },
        ),
    ]