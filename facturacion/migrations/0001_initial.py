# Generated by Django 2.0.6 on 2018-07-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteCab',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('cffecdoc', models.DateTimeField(blank=True, db_column='CFFECDOC', null=True)),
                ('raz_social_emisor', models.CharField(blank=True, db_column='RAZ_SOCIAL_EMISOR', max_length=100, null=True)),
                ('nom_comercial_emisor', models.CharField(blank=True, db_column='NOM_COMERCIAL_EMISOR', max_length=100, null=True)),
                ('ubigeo_emisor', models.CharField(blank=True, db_column='UBIGEO_EMISOR', max_length=6, null=True)),
                ('direccion_emisor', models.CharField(blank=True, db_column='DIRECCION_EMISOR', max_length=100, null=True)),
                ('urbanizacion_emisor', models.CharField(blank=True, db_column='URBANIZACION_EMISOR', max_length=25, null=True)),
                ('provincia_emisor', models.CharField(blank=True, db_column='PROVINCIA_EMISOR', max_length=30, null=True)),
                ('departamento_emisor', models.CharField(blank=True, db_column='DEPARTAMENTO_EMISOR', max_length=30, null=True)),
                ('distrito_emisor', models.CharField(blank=True, db_column='DISTRITO_EMISOR', max_length=30, null=True)),
                ('pais_emisor', models.CharField(blank=True, db_column='PAIS_EMISOR', max_length=2, null=True)),
                ('ruc_emisor', models.CharField(blank=True, db_column='RUC_EMISOR', max_length=11, null=True)),
                ('tip_doc_emisor', models.CharField(blank=True, db_column='TIP_DOC_EMISOR', max_length=1, null=True)),
                ('serie_nc_nd', models.CharField(blank=True, db_column='SERIE_NC_ND', max_length=4, null=True)),
                ('nro_compr_nc_nd', models.CharField(blank=True, db_column='NRO_COMPR_NC_ND', max_length=8, null=True)),
                ('tip_nc_nd', models.CharField(blank=True, db_column='TIP_NC_ND', max_length=2, null=True)),
                ('motivo_nc_nd', models.CharField(blank=True, db_column='MOTIVO_NC_ND', max_length=250, null=True)),
                ('tip_doc_modif_nc_nd', models.CharField(blank=True, db_column='TIP_DOC_MODIF_NC_ND', max_length=2, null=True)),
                ('tipodoc_comprobante', models.CharField(blank=True, db_column='TIPODOC_COMPROBANTE', max_length=2, null=True)),
                ('cfnumser', models.CharField(db_column='CFNUMSER', max_length=4)),
                ('cfnumdoc', models.CharField(db_column='CFNUMDOC', max_length=8)),
                ('tip_doc_receptor', models.CharField(blank=True, db_column='TIP_DOC_RECEPTOR', max_length=1, null=True)),
                ('nro_doc_receptor', models.CharField(blank=True, db_column='NRO_DOC_RECEPTOR', max_length=15, null=True)),
                ('cfcodcli', models.CharField(blank=True, db_column='CFCODCLI', max_length=11, null=True)),
                ('cfnombre', models.CharField(blank=True, db_column='CFNOMBRE', max_length=100, null=True)),
                ('direccion_receptor', models.CharField(blank=True, db_column='DIRECCION_RECEPTOR', max_length=100, null=True)),
                ('tvv_cod_ope_gravadas', models.CharField(blank=True, db_column='TVV_COD_OPE_GRAVADAS', max_length=4, null=True)),
                ('tvv_imp_ope_gravadas', models.DecimalField(db_column='TVV_IMP_OPE_GRAVADAS', decimal_places=2, max_digits=12)),
                ('tvv_cod_ope_inafectas', models.CharField(blank=True, db_column='TVV_COD_OPE_INAFECTAS', max_length=4, null=True)),
                ('tvv_imp_ope_inafectas', models.DecimalField(db_column='TVV_IMP_OPE_INAFECTAS', decimal_places=2, max_digits=12)),
                ('tvv_cod_ope_exoneradas', models.CharField(blank=True, db_column='TVV_COD_OPE_EXONERADAS', max_length=4, null=True)),
                ('tvv_imp_ope_exoneradas', models.DecimalField(db_column='TVV_IMP_OPE_EXONERADAS', decimal_places=2, max_digits=12)),
                ('sumatoria_igv', models.DecimalField(db_column='SUMATORIA_IGV', decimal_places=2, max_digits=12)),
                ('cod_tributo_igv', models.CharField(blank=True, db_column='COD_TRIBUTO_IGV', max_length=4, null=True)),
                ('nom_tributo_igv', models.CharField(blank=True, db_column='NOM_TRIBUTO_IGV', max_length=6, null=True)),
                ('cod_inter_igv', models.CharField(blank=True, db_column='COD_INTER_IGV', max_length=3, null=True)),
                ('sumatoria_isc', models.DecimalField(db_column='SUMATORIA_ISC', decimal_places=2, max_digits=12)),
                ('cod_tributo_isc', models.CharField(blank=True, db_column='COD_TRIBUTO_ISC', max_length=4, null=True)),
                ('nom_tributo_isc', models.CharField(blank=True, db_column='NOM_TRIBUTO_ISC', max_length=6, null=True)),
                ('cod_inter_isc', models.CharField(blank=True, db_column='COD_INTER_ISC', max_length=3, null=True)),
                ('sumatoria_otros_trib', models.DecimalField(db_column='SUMATORIA_OTROS_TRIB', decimal_places=2, max_digits=12)),
                ('cod_tributo_otros_trib', models.CharField(blank=True, db_column='COD_TRIBUTO_OTROS_TRIB', max_length=4, null=True)),
                ('nom_tributo_otros_trib', models.CharField(blank=True, db_column='NOM_TRIBUTO_OTROS_TRIB', max_length=6, null=True)),
                ('cod_inter_otros_trib', models.CharField(blank=True, db_column='COD_INTER_OTROS_TRIB', max_length=3, null=True)),
                ('sumatoria_otros_cargos', models.DecimalField(db_column='SUMATORIA_OTROS_CARGOS', decimal_places=2, max_digits=12)),
                ('cod_tip_dsctos', models.CharField(blank=True, db_column='COD_TIP_DSCTOS', max_length=4, null=True)),
                ('importe_dsctos', models.DecimalField(db_column='IMPORTE_DSCTOS', decimal_places=2, max_digits=12)),
                ('importe_total_venta', models.DecimalField(db_column='IMPORTE_TOTAL_VENTA', decimal_places=2, max_digits=12)),
                ('serie_guia', models.CharField(blank=True, db_column='SERIE_GUIA', max_length=4, null=True)),
                ('nro_guia', models.CharField(blank=True, db_column='NRO_GUIA', max_length=8, null=True)),
                ('cod_tipo_guia', models.CharField(blank=True, db_column='COD_TIPO_GUIA', max_length=2, null=True)),
                ('serie_otro_refe', models.CharField(blank=True, db_column='SERIE_OTRO_REFE', max_length=4, null=True)),
                ('nro_otro_refe', models.CharField(blank=True, db_column='NRO_OTRO_REFE', max_length=8, null=True)),
                ('cod_tipo_refe', models.CharField(blank=True, db_column='COD_TIPO_REFE', max_length=2, null=True)),
                ('cod_percepcion', models.CharField(blank=True, db_column='COD_PERCEPCION', max_length=4, null=True)),
                ('baseimponible_percepcion', models.DecimalField(db_column='BASEIMPONIBLE_PERCEPCION', decimal_places=2, max_digits=12)),
                ('monto_percepcion', models.DecimalField(db_column='MONTO_PERCEPCION', decimal_places=2, max_digits=12)),
                ('totalcobrado_percepcion', models.DecimalField(db_column='TOTALCOBRADO_PERCEPCION', decimal_places=2, max_digits=12)),
                ('ubl_version', models.CharField(blank=True, db_column='UBL_VERSION', max_length=10, null=True)),
                ('estruc_version', models.CharField(blank=True, db_column='ESTRUC_VERSION', max_length=10, null=True)),
                ('tvv_cod_ope_gratuitas', models.CharField(blank=True, db_column='TVV_COD_OPE_GRATUITAS', max_length=4, null=True)),
                ('tvv_imp_ope_gratuitas', models.DecimalField(db_column='TVV_IMP_OPE_GRATUITAS', decimal_places=2, max_digits=15)),
                ('descuentos_globales', models.DecimalField(db_column='DESCUENTOS_GLOBALES', decimal_places=2, max_digits=12)),
                ('estado_comprobante', models.CharField(blank=True, db_column='ESTADO_COMPROBANTE', max_length=150, null=True)),
                ('moneda', models.CharField(blank=True, db_column='MONEDA', max_length=3, null=True)),
                ('cdr', models.CharField(blank=True, db_column='CDR', max_length=50, null=True)),
                ('cod_resumen', models.CharField(blank=True, db_column='COD_RESUMEN', max_length=20, null=True)),
                ('cod_baja', models.CharField(db_column='COD_BAJA', max_length=20)),
                ('ruta_comprobante', models.CharField(blank=True, db_column='RUTA_COMPROBANTE', max_length=4000, null=True)),
                ('ruta_cdr', models.CharField(blank=True, db_column='RUTA_CDR', max_length=4000, null=True)),
                ('tipo_envio', models.CharField(blank=True, db_column='TIPO_ENVIO', max_length=10, null=True)),
                ('correo', models.CharField(blank=True, db_column='CORREO', max_length=100, null=True)),
                ('leyenda', models.CharField(blank=True, db_column='LEYENDA', max_length=250, null=True)),
                ('glosa_electronica', models.CharField(blank=True, db_column='GLOSA_ELECTRONICA', max_length=250, null=True)),
                ('cod_cat_detraccion', models.CharField(blank=True, db_column='COD_CAT_DETRACCION', max_length=5, null=True)),
                ('porcentaje_detraccion', models.CharField(blank=True, db_column='PORCENTAJE_DETRACCION', max_length=18, null=True)),
                ('monto_detraccion', models.DecimalField(blank=True, db_column='MONTO_DETRACCION', decimal_places=2, max_digits=12, null=True)),
                ('valor_referencial_detraccion', models.DecimalField(blank=True, db_column='VALOR_REFERENCIAL_DETRACCION', decimal_places=2, max_digits=12, null=True)),
                ('cod_cat_bbss_detraccion', models.CharField(blank=True, db_column='COD_CAT_BBSS_DETRACCION', max_length=5, null=True)),
                ('codigo_bbss_detraccion', models.CharField(blank=True, db_column='CODIGO_BBSS_DETRACCION', max_length=5, null=True)),
                ('cod_cat_cta_bn_detraccion', models.CharField(blank=True, db_column='COD_CAT_CTA_BN_DETRACCION', max_length=5, null=True)),
                ('cta_bn_detraccion', models.CharField(blank=True, db_column='CTA_BN_DETRACCION', max_length=15, null=True)),
                ('total_anticipo', models.DecimalField(db_column='TOTAL_ANTICIPO', decimal_places=2, max_digits=15)),
                ('tipo_operacion', models.CharField(blank=True, db_column='TIPO_OPERACION', max_length=3, null=True)),
                ('estado_correo', models.CharField(blank=True, db_column='ESTADO_CORREO', max_length=50, null=True)),
                ('ordencompra', models.CharField(blank=True, db_column='ORDENCOMPRA', max_length=20, null=True)),
                ('usuario', models.CharField(blank=True, db_column='USUARIO', max_length=20, null=True)),
                ('codigopventa', models.CharField(blank=True, db_column='CODIGOPVENTA', max_length=20, null=True)),
                ('placa', models.CharField(blank=True, db_column='PLACA', max_length=50, null=True)),
                ('xml', models.TextField(blank=True, db_column='XML', null=True)),
                ('ubigeo_pventa', models.CharField(blank=True, db_column='UBIGEO_PVENTA', max_length=12, null=True)),
                ('direccion_pventa', models.CharField(blank=True, db_column='DIRECCION_PVENTA', max_length=200, null=True)),
                ('urbanizacion_pventa', models.CharField(blank=True, db_column='URBANIZACION_PVENTA', max_length=50, null=True)),
                ('provincia_pventa', models.CharField(blank=True, db_column='PROVINCIA_PVENTA', max_length=60, null=True)),
                ('departamento_pventa', models.CharField(blank=True, db_column='DEPARTAMENTO_PVENTA', max_length=60, null=True)),
                ('distrito_pventa', models.CharField(blank=True, db_column='DISTRITO_PVENTA', max_length=60, null=True)),
                ('pais_pventa', models.CharField(blank=True, db_column='PAIS_PVENTA', max_length=2, null=True)),
            ],
            options={
                'db_table': 'COMPROBANTE_CAB',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ComprobanteDet',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dfnumser', models.CharField(db_column='DFNUMSER', max_length=4)),
                ('dfnumdoc', models.CharField(db_column='DFNUMDOC', max_length=8)),
                ('tipodoc_comprobante', models.CharField(db_column='TIPODOC_COMPROBANTE', max_length=2)),
                ('orden_item', models.IntegerField(db_column='ORDEN_ITEM')),
                ('um_item', models.CharField(blank=True, db_column='UM_ITEM', max_length=6, null=True)),
                ('cant_item', models.DecimalField(db_column='CANT_ITEM', decimal_places=10, max_digits=18)),
                ('nom_item', models.CharField(blank=True, db_column='NOM_ITEM', max_length=250, null=True)),
                ('vu_item', models.DecimalField(db_column='VU_ITEM', decimal_places=2, max_digits=12)),
                ('imp_vu_item', models.DecimalField(db_column='IMP_VU_ITEM', decimal_places=2, max_digits=12)),
                ('cod_vu_item', models.CharField(blank=True, db_column='COD_VU_ITEM', max_length=2, null=True)),
                ('monto_igv', models.DecimalField(db_column='MONTO_IGV', decimal_places=2, max_digits=12)),
                ('afec_igv', models.CharField(blank=True, db_column='AFEC_IGV', max_length=2, null=True)),
                ('cod_igv', models.CharField(blank=True, db_column='COD_IGV', max_length=4, null=True)),
                ('nom_igv', models.CharField(blank=True, db_column='NOM_IGV', max_length=6, null=True)),
                ('cinter_igv', models.CharField(blank=True, db_column='CINTER_IGV', max_length=3, null=True)),
                ('monto_isc', models.DecimalField(db_column='MONTO_ISC', decimal_places=2, max_digits=12)),
                ('afec_isc', models.CharField(blank=True, db_column='AFEC_ISC', max_length=2, null=True)),
                ('cod_isc', models.CharField(blank=True, db_column='COD_ISC', max_length=4, null=True)),
                ('nom_isc', models.CharField(blank=True, db_column='NOM_ISC', max_length=6, null=True)),
                ('cinter_isc', models.CharField(blank=True, db_column='CINTER_ISC', max_length=3, null=True)),
                ('tvu_item', models.DecimalField(db_column='TVU_ITEM', decimal_places=2, max_digits=12)),
                ('cod_item', models.CharField(blank=True, db_column='COD_ITEM', max_length=30, null=True)),
                ('importe_nooneroso_item', models.DecimalField(db_column='IMPORTE_NOONEROSO_ITEM', decimal_places=2, max_digits=12)),
                ('cod_nooneroso_item', models.CharField(blank=True, db_column='COD_NOONEROSO_ITEM', max_length=2, null=True)),
                ('false_item', models.CharField(blank=True, db_column='FALSE_ITEM', max_length=5, null=True)),
                ('des_item', models.DecimalField(db_column='DES_ITEM', decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'COMPROBANTE_DET',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoComprobante',
            fields=[
                ('idTipoComprobante', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('numDocUsuario', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('rznSocialUsuario', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='comprobantedet',
            unique_together={('dfnumser', 'dfnumdoc', 'tipodoc_comprobante', 'orden_item')},
        ),
        migrations.AlterUniqueTogether(
            name='comprobantecab',
            unique_together={('cfnumser', 'cfnumdoc', 'tipodoc_comprobante')},
        ),
    ]
