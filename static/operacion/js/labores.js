$(document).on('ready', function(){
  $('#addlabor').modal();
  $('.addlabor').on('click', function(event){return false;});
  $('.addlabor').on('click', function(event){
    // $("#contenido").load($(this).attr('href'),function(responseTxt, statusTxt, xhr){
    //       console.log(statusTxt+"   Error: " + xhr.status + ": " + xhr.statusText);
    //       $('#id_empleado').material_select();
    //       $('#addempleado').modal('open');
    // });
    //document.getElementById('form_labor').reset()
    $('#form_labor label[for="mensaje"]').text("");
    var user =$('#user').val(),
        pass = $('#password').val();
        console.log("proceso de autenticacion "+user+"  "+pass);
    $.ajax({
      url:$(this).attr('href'),
      type:'post',
      dataType:'json',
      data:{user:user,pass:pass},
      success:function(data){
        console.log(data);
        if (!data[0].status){
          document.getElementById('form_labor').reset()
          $('#form_labor label[for="mensaje"]').text("Clave y usuario invalidos");
        }
        $.ajax({
          url:$('#form_labor').attr('action'),
          type:'post',
          dataType:'json',
          data:{usuario:data[0].id},
          success:function(data){
            if (!data[0].status){
              document.getElementById('form_labor').reset()
              $('#form_labor label[for="mensaje"]').text("Clave y usuario invalidos");
            }else{
              $('#form_labor').modal('close');
            }
          }
        });
      }
    });
  });
});
