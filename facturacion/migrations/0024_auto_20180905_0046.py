# Generated by Django 2.0.6 on 2018-09-05 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0023_auto_20180905_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobantecab',
            name='estado_comprobante',
            field=models.ForeignKey(blank=True, db_column='ESTADO_COMPROBANTE', max_length=20, null=True, on_delete=False, to='facturacion.EstadoDocumento'),
        ),
    ]