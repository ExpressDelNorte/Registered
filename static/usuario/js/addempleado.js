$(document).on('ready', function(){
  $('.addempleado').on('click', function(event){
    return false;
  });
  $('.addempleado').on('click', function(event){
    $("#contenido").load($(this).attr('href'),function(responseTxt, statusTxt, xhr){
          alert(statusTxt+"   Error: " + xhr.status + ": " + xhr.statusText);
          $('#addempleado').modal('open');
    });
  });
});
