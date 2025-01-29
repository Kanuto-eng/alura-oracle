alert("¡Bienvenida y bienvenido a nuestro sitio web!");

let nombre_ = "Lua";
//console.log(nombre_);
let edad_ = 25;
//console.log(edad_);
let numeroDeVentas = 50;
//console.log(numeroDeVentas);
let saldoDisponible = 1000;
//console.log(saldoDisponible);
let mensajeDeError = alert ("¡Error! Completa todos los campos");
//console.log(mensajeDeError);

let nombre = prompt("Me indicas tu nombre por favor:");
let edad = prompt("Me indicas tu edad por favor:");

if (edad >= 18) {
    alert(nombre  + " ¡Puedes obtener tu licencia de conducir tienes! " + edad);
} else {
    alert(nombre  + " No puedes obtener tu licencia de conducir tienes " + edad);
}