var pagina=0,proxima=0,bandera=true,b2=true,TOTAL_REGISTROS=0;
var fecha1=null,fecha2=null;
$(document).on('ready', function(){
  listLabores();
});
function listLabores(){
      $.ajax({
        url:'/operacion/list/labor/',
        type:'get',
        dataType:'json',
        success:function(data){
          console.log(data);
          var emp = $('#tab_emp');
          emp.html("");
          var resul = data.object_list;
          if(resul.length){
            var limite=0,inicio=0;
            if (proxima == 0){
              limite=5;
              incio=0;
            }else{
              limite = proxima*5;
              inicio = (proxima-1)*5;
            }
            TOTAL_REGISTROS = data.count;
            var fecha_Actual = new Date();
            for(var i=inicio;i < limite;i++){
              if (i < TOTAL_REGISTROS){
                var identificacion = resul[i].identificacion,
                    nombre = resul[i].nombre,
                    apellidos = resul[i].apellidos,
                    inicio = resul[i].ini,
                    id = resul[i].id,
                    tiempo = resul[i].tiempo,
                    temporal="";
                    temporal+="<td>"+identificacion+"</td>";
                    temporal+="<td>"+nombre+"</td>";
                    temporal+="<td>"+apellidos+"</td>";
                    temporal+="<td>"+inicio+"</td>";
                    temporal+="<td><label class=\"move_time\">"+parseFloat(calcularTiempo(inicio, fecha_Actual)).toFixed(2)+"</label><input type=\"hidden\" name=\"time\" value=\""+tiempo+"\"></td>";
                    var d= "<ul class=\"tabla_tool\">";
                    d+="<li><a href =\""+resul[i].servicios.edit+"\" class=\"btn-floating red tabla_edit\"><i class=\"material-icons\">edit</i></a></li>";
                    temporal+="<td>"+d+"</td>";
                    emp.append("<tr>"+temporal+"</tr>");
                }
            }
            var paginador = $('#paginador');
            paginador.html("");
            paginador.append('<li class="disabled"><a href="#!" class=\"ant\"><i class="material-icons">chevron_left</i></a></li>');
            console.log(data.next);
            if( bandera){
              console.log(data.count,' valor de impresion ',data.count/5);
              paginas = Math.round(data.count/5);
              proxima = data.next;
              if (paginas < 1){
                paginas =1;
                proxima=1;
              }
              bandera=false;
              // var paginador = $('#paginador');
              // paginador.html("");
              // paginador.append('<li class="disabled"><a href="#!" class=\"ant\"><i class="material-icons">chevron_left</i></a></li>');
            }else{
              //borrar el iterador
            }
            for(var i=0; i< paginas;i++){
              var clase="";
              if (b2){
                  clase = (i+1 == proxima-1?"active":"waves-effect");
              }else{
                clase = (i+1 == proxima?"active":"waves-effect");
              }
              paginador.append("<li class=\""+clase+"\"><a href=\""+(1+i)+"\" class=\"iterator\">"+(1+i)+"</a></li>");
            }
            b2=false;
            paginador.append('<li class="waves-effect"><a href="#!" class=\"sig\"><i class="material-icons">chevron_right</i></a></li>');
            $('.tabla_delete, .tabla_edit').on('click', function(event){
              return false;
            });
            $('.tabla_delete').on('click', function(event){
              console.log("desde los tool tabla");
            });
            $('.tabla_edit').on('click', function(event){
              console.log("desde los tool tabla");
            });
            eventosDePaginador();
          }
        }
      });
  //  }
}

function eventosDePaginador(){
  $('.iterator').on('click', function(event){
    return false;
  });
  $('.iterator').on('click', function(event){
    proxima = $(this).attr('href');
    $('.pagination li').removeClass('active');
    var actual = $('.pagination li.active');
    actual.removeClass('active');
    actual.addClass('waves-effect');
    var proximo = $(".pagination li a[href=\""+proxima+"\"");
    console.log("El cambio de elmento es ",proximo);
    proximo.parent().addClass('active');
    proximo.parent().removeClass('waves-effect');
    listLabores();
  });
}

function calcularTiempo(valor,fechaActual){
  fecha1 = fechaActual;
  var men = valor;
  console.log(men);
  var contenedor = men.split(" ");
  console.log(contenedor);
  var fecha = contenedor[0].split("/");
  console.log(fecha);
  var h = contenedor[1].split(':');
  console.log(h);
  var hora = h[0];
  console.log(hora);
  var minutos = h[1].substring(0, 2);
  var notacion = h[1].substring(2,4);
  var c = notacion=="PM"?String(parseInt(hora)+12) : hora ;
  var date_armado = new Date(fecha[2]+"-"+fecha[1]+"-"+fecha[0]+" "+c+":"+minutos+":00 UTC-5");
  fecha2 = date_armado;
  return (fechaActual.getTime()-date_armado.getTime())/1000/(60*60);
}
