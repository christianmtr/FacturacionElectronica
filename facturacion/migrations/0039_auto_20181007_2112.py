# Generated by Django 2.0.6 on 2018-10-08 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0038_locales'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parametro',
            new_name='EmpresaParametro',
        ),
        migrations.RenameModel(
            old_name='Locales',
            new_name='Local',
        ),
        migrations.AlterModelOptions(
            name='empresaparametro',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='local',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='empresaparametro',
            table='EMPRESA_PARAMETRO',
        ),
        migrations.AlterModelTable(
            name='local',
            table='LOCAL',
        ),
    ]
