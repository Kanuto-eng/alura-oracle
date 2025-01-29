// funcion para numeros aleatorios usando math
function aleatorios( min, max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}
//variables para numeros
let numeroSecreto = aleatorios(1, 10); // numeros aleatorios entre 1 - 10 elegidos por la pc
let numeroUsuario = 0;
let intentos = 1; // numero minimo de intentos para ganar
let maxIntentos = 5; // numero maximo de intentos para ganar

while(numeroUsuario != numeroSecreto){
        numeroUsuario = parseInt(prompt("Me indicas un numero entre 1 y 10 por favor:"));

        //comparacion de numeros de usuarios vs computadora

        if (numeroUsuario == numeroSecreto) {
                alert(`Correcto! acertaste el numero, El numero secreto era  ${numeroSecreto} lo hiciste en ${intentos} ${intentos == 1 ? 'intento' : 'intentos'}` );
        } else {
                if (numeroUsuario > numeroSecreto) {
                alert('El numero secreto es menor')
                } else {
                alert('El numero secreto es mayor')
                }
        }
        //aumento de intentos cuando no acierta
        intentos += 1;

        //rompe el bucle cuando se acaban los intentos
        if (intentos > maxIntentos){
                alert (`Has llegado al limite de  intentos ${maxIntentos}`);
                break;
        }
}


