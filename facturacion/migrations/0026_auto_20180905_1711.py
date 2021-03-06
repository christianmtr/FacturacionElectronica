# Generated by Django 2.0.6 on 2018-09-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0025_comprobantecab_estado_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobantecab',
            name='estado_comprobante',
            field=models.ForeignKey(blank=True, db_column='ESTADO_COMPROBANTE', default='00', max_length=20, null=True, on_delete=False, to='facturacion.EstadoDocumento'),
        ),
        migrations.AlterField(
            model_name='comprobantedet',
            name='porcent_igv',
            field=models.DecimalField(blank=True, db_column='PORCENT_IGV', decimal_places=2, default=18.0, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='comprobantedet',
            name='porcent_isc',
            field=models.DecimalField(blank=True, db_column='PORCENT_ISC', decimal_places=2, default=15.0, max_digits=5, null=True),
        ),
    ]
