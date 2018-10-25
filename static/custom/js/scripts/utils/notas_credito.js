$utils.notas_credito.datatableContenido = undefined;
$utils.notas_credito.datatable = undefined;
$utils.notas_credito.datatableDetalle = undefined;
$utils.notas_credito.cfnumser=undefined
$utils.notas_credito.cfnumdoc=undefined
$utils.notas_credito.tipodoc=undefined
$utils.notas_credito.nomArchivo='';
$utils.notas_credito.TIPOCOMPROBANTE='07';


$utils.notas_credito.crearTablaComprobantes=function(tabla,fechaIni,fechaFin,estado){
        var columns = [
                    {data: 'cffecdoc' ,'searchable':false},
                    {data:'cfnumser' ,'searchable':true},
                    {data:'cfnumdoc' ,'searchable':true},
                    {data: 'cfnombre' ,'searchable':true},
                    {data: 'estado_comprobante' ,'searchable':true},


        ];
        var slug = 'facturacion-api/comprobantes/listar';
        var serie=$('#serie').val();
        var numdoc=$('#numdoc').val();
        var razonsocial=$('#razonsocial').val();

        //var fecha =$('#fecha').attr('valor');
        var fechaIni =fechaIni;
        var fechaFin =fechaFin;
        var data={
            'serie':serie,
            'numdoc':numdoc,
            'razonsocial':razonsocial,
            'tipodoc':$utils.notas_credito.TIPOCOMPROBANTE,
            'estado':estado,
            'fechaIni':fechaIni,
            'fechaFin':fechaFin
        }

        if (!($utils.notas_credito.datatableContenido === undefined))
        {$utils.notas_credito.datatableContenido.destroy();}

        $utils.notas_credito.datatableContenido = tabla.DataTable({

            "processing": true,
            "serverSide": true,

            "ajax":{
                url: $utils.urlServer(slug),
                "data": data,


            },
            createdRow: function (row, data, dataIndex) {
                  $(row).attr('cfnumser',data.cfnumser);
                  $(row).attr('cfnumdoc',data.cfnumdoc);
                  $(row).attr('tipodoc_comprobante',data.tipodoc_comprobante);
                },

                bLengthChange: false,
                bPaginate: true,
                bInfo: false,
                scrollY: "500px",
                autoWidth: true,
                ordering: false,
                searching: false,
                fixedRowHeight:false,
                scrollX: false,
                bInfo: true,
                iDisplayLength: 10,
                columns:columns,
        });

    }


$utils.notas_credito.crearTablaDetalleComprobante = function (tabla, data) {
        if (!($utils.notas_credito.datatableDetalle === undefined)) {
        $utils.notas_credito.datatableDetalle.destroy();
        }

        $utils.notas_credito.datatableDetalle = tabla.DataTable({
                "data": data,
                 columns: [

                    {data: 'orden_item' },
                    {data: 'cant_item' },
                    {data: 'um_item' },
                    {data: 'cod_item'  },
                    {data: 'nom_item'  },
                    {data: 'imp_vu_item' },
                    {data: 'imp_total_item' },

                ],

                bLengthChange: false,
                bPaginate: false,
                bInfo: false,
                scrollY: "100px",
                autoWidth: false,
                ordering: false,
                searching: false,
                scrollX: true,
        });
}





$utils.notas_credito.crearDetalleComprobante = function (cell, tabla) {

    var $row = $(cell).closest('tr');
    var cfnumser=$row.attr('cfnumser');
    var cfnumdoc=$row.attr('cfnumdoc');
    var tipodoc=$row.attr('tipodoc_comprobante');
    $utils.notas_credito.cfnumser = cfnumser;
    $utils.notas_credito.cfnumdoc = cfnumdoc;
    $utils.notas_credito.tipodoc  = tipodoc ;

    var datax={
    'cfnumser'            : cfnumser ,
    'cfnumdoc'            : cfnumdoc  ,
    'tipodoc_comprobante' : tipodoc,
    'csrfmiddlewaretoken' : App.csrf_token,
    }



    $services.comprobante.getComprobante(datax,function (data){

        $('#cffecdoc').val(data.cabecera.cffecdoc);
        $('#cfnumdoc').val(data.cabecera.cfnumdoc);
        $('#estado_comprobante').val(data.cabecera.estado_comprobante);
        $('#cfcodcli').val(data.cabecera.cfcodcli);
        $('#nro_doc_receptor').val(data.cabecera.nro_doc_receptor);
        $('#cfnombre').val(data.cabecera.cfnombre);
        $('#moneda').val(data.cabecera.moneda);

        $('#tvv_cod_ope_exoneradas').val(data.cabecera.tvv_imp_ope_exoneradas);
        $('#total').val(data.cabecera.tvv_imp_ope_gravadas);
        $('#tvv_imp_ope_gravadas').val(data.cabecera.tvv_imp_ope_gravadas);
        $('#tvv_imp_ope_inafectas').val(data.cabecera.tvv_imp_ope_inafectas);
        $('#sumatoria_igv').val(data.cabecera.sumatoria_igv);
        $('#sumatoria_isc').val(data.cabecera.sumatoria_isc);
        $('#importe_total_venta').val(data.cabecera.importe_total_venta);
        $utils.notas_credito.nomArchivo=data.cabecera.nom_archivo;
        $utils.notas_credito.crearTablaDetalleComprobante(tabla,data.detalle);

    });
    $('#modal_detalle_factura').modal("show");
}


$utils.notas_credito.descargarPdf = function () {

    /*var cfnumser=$utils.notas_credito.cfnumser;
    var cfnumdoc=$utils.notas_credito.cfnumdoc;
    var tipodoc =$utils.notas_credito.tipodoc ;
*/
    $services.comprobante.descargarPdf($utils.notas_credito.nomArchivo,function (error){

        if(error==true){
            swal('No se puede descargar el archivo, es posible q no exista');
        }
    });
}



$utils.notas_credito.descargarXml = function () {
    /*var cfnumser=$utils.notas_credito.cfnumser;
    var cfnumdoc=$utils.notas_credito.cfnumdoc;
    var tipodoc =$utils.notas_credito.tipodoc ;
*/
    $services.comprobante.descargarXml($utils.notas_credito.nomArchivo,function (error){
        if(error==true){
            swal('No se puede descargar el archivo, es posible q no exista');
        }
    });
}

$utils.notas_credito.crearCombo = function (select){
    var html='<option value="" selected>TODOS</option>';
    $services.comprobante.getEstadosDocumentos(function (data) {
        data.forEach(function (el) {
            html+='<option value="'+el.id+'">'+el.nombre+'</option>';
        })
        select.html(html);
    });
}

