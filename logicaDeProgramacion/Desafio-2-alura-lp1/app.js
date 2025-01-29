//Pregunta al usuario qué día de la semana es. Si la respuesta es "Sábado" o "Domingo", muestra "¡Buen fin de semana!". De lo contrario, muestra "¡Buena semana!".

let diaDeLaSemana = prompt('Puedes decirme que dia de la semana es: ');
let dia = diaDeLaSemana;

if (dia === "sabado" || dia === "domingo"){
    alert("😊 ¡Buen fin de semana!");
} else {
    alert("😒 ¡Buena semana!.");
}

console.log("El día elegido es: " + dia);

//Verifica si un número ingresado por el usuario es positivo o negativo. Muestra una alerta informativa.

let numeroIngresado = prompt('Por favor ingresa un número: ');

if (numeroIngresado > 0){
    alert('El número ingresado es positivo.');
} else if (numeroIngresado < 0){
    alert('El número ingresado es negativo.');
} else {
    alert('El número ingresado es cero.');
}

//  Crea un sistema de puntuación para un juego. Si la puntuación es mayor o igual a 100, muestra "¡Felicidades, has ganado!". En caso contrario, muestra "Intentalo nuevamente para ganar.".

let puntaje = prompt('Por favor ingresa tu puntaje que sacaste en el juego de adivinar: ');

if (puntaje >= 100){
    alert('😍 Felicidades, has ganado!');
} else {
    alert('😒 Intentalo nuevamente para ganar.');
}

// Crea un mensaje que informe al usuario sobre el saldo de su cuenta, utilizando un template string para incluir el valor del saldo.

let dineroARetirar = prompt('Ingresa un valor del dinero a retirar');
let dineroCuenta = 1000000
let saldoActual =  dineroCuenta - dineroARetirar;

if (dineroARetirar <= 1000 && dineroCuenta == 0){
    alert('No puedes retirar esa cantidad. Debes retirar al menos $1000.');
} else if (dineroARetirar > 1000 && dineroARetirar <= 5000){
    alert('Has retirado un monto aceptable. Tu saldo actual es: $' + saldoActual);
} else if (dineroARetirar > 5000 && dineroARetirar <= 1000000){
    alert('Has retirado un monto muy grande. Tu saldo actual es: $' + saldoActual);
} else {
    alert('No tienes fondos suficientes. Tu saldo actual es: $' + saldoActual);
}

let mensajeSaldo = (`Restiraste : ${dineroARetirar}, Tu saldo actual es: ${saldoActual}`);

alert(mensajeSaldo);

//Pide al usuario que ingrese su nombre mediante un prompt. Luego, muestra una alerta de bienvenida usando ese nombre.

let nombreUsuario = prompt('Por favor ingresa tu nombre: ');

alert(`😘 Hola ${nombreUsuario}! Bienvenido a pagina web.`);
