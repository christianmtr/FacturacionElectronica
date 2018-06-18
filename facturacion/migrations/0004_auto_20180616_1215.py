# Generated by Django 2.0.6 on 2018-06-16 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20180616_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallefacturaelectronica',
            name='numFactura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='facturacion.FacturaElectronica'),
        ),
        migrations.AlterField(
            model_name='facturaelectronica',
            name='numDocUsuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='facturacion.Usuario'),
        ),
    ]
