# Generated by Django 2.0.6 on 2018-07-18 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0005_comprobantecab_estado_anula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprobantecab',
            name='estado_anula',
        ),
        migrations.RemoveField(
            model_name='comprobantecab',
            name='fec_anula',
        ),
        migrations.RemoveField(
            model_name='comprobantecab',
            name='flg_anula',
        ),
        migrations.RemoveField(
            model_name='comprobantecab',
            name='motivo_anula',
        ),
    ]
