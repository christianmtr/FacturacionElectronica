# Generated by Django 2.0.6 on 2018-09-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0013_resumendet_ruc_emisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumendet',
            name='raz_social_emisor',
            field=models.CharField(blank=True, db_column='RAZ_SOCIAL_EMISOR', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resumendet',
            name='tip_doc_emisor',
            field=models.CharField(blank=True, db_column='TIP_DOC_EMISOR', max_length=1, null=True),
        ),
    ]
