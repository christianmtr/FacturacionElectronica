# Generated by Django 2.0.6 on 2018-09-03 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0017_estadodocumentosunat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EstadoDocumentoSunat',
            new_name='EstadoDocumento',
        ),
        migrations.AlterModelTable(
            name='estadodocumento',
            table='ESTADO_DOCUMENTO',
        ),
    ]
