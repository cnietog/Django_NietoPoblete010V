
function act() {
$(document).ready(function(){

    $("#enviar").click(function(){

        $.get("https://apis.digital.gob.cl/fl/feriados/2022",function(data){

            $.each(data,function(i,item)
                {
                    $("#categorias").append("<tr><td>"+ item.nombre +
                    "</td><td>"+ item.fecha +
                    "</td><td>"+item.tipo+"</td></tr>");
                  
                });


        });

    });
});
}
function actual() {
 fecha=new Date(); //Actualizar fecha.
 hora=fecha.getHours(); //hora actual
 minuto=fecha.getMinutes(); //minuto actual
 segundo=fecha.getSeconds(); //segundo actual
 if (hora<10) { //dos cifras para la hora
    hora="0"+hora;
    }
 if (minuto<10) { //dos cifras para el minuto
    minuto="0"+minuto;
    }
 if (segundo<10) { //dos cifras para el segundo
    segundo="0"+segundo;
    }
 //ver en el recuadro del reloj:
 mireloj = hora+" : "+minuto+" : "+segundo;	
         return mireloj; 
 }
function actualizar() { //función del temporizador
  mihora=actual(); //recoger hora actual
  mireloj=document.getElementById("reloj"); //buscar elemento reloj
  mireloj.innerHTML=mihora; //incluir hora en elemento
    }
setInterval(actualizar,1000); //iniciar temporizador





$(function() 
{
  $("#mi-formulario").validate({
       rules: {
              user:"required",
              email: {
                  required: true,
                  email: true
              },
              password: "required",
              fono: "required",
              password2: {
                  required: true,
                  equalTo: "#password"
              }   
              
          }, //rules
      messages: {
          user:{
            required: 'Ingresa tu usuario'
          },
          email: {
              required: 'Ingresa tu correo electrónico',
              email: 'Formato de correo no válido'
          },
          password: {
              required: 'Ingresa una contraseña',
              minlength: 'Caracteres insuficientes'
          },
          fono:{
              required: 'Ingrese un número de celular',
              minlength: 'Cantidad de digitos insuficiente'
          },
          password2: {
              required: 'Reingresa la contraseña',
              equalTo: 'Las contraseñas ingresadas no coinciden',
              minlength: 'Caracteres insuficientes'

          }
      }//messages
  }); //$('#mi-formulario').validate
}); //function



