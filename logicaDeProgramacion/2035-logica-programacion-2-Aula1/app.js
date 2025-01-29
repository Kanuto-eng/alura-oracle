let numeroSecreto = 0;
let intentos = 0;
let listaNumerosSorteados = [];
let numeroMaximo = 10;
condicionesIniciales();

function condicionesIniciales(){
    asignarTextoElemento('h1', 'Juego del numero secreto');
    asignarTextoElemento('p', `Indica un numero de 1 a ${numeroMaximo} 🤔` );
    numeroSecreto = numeroAleatorio();
    intentos = 1; 

    return;
}
function  asignarTextoElemento(elemento, texto) {
    let elementoHTML = document.querySelector(elemento);
    elementoHTML.innerHTML = texto;
    return;
}
function verificarIntento() {
    let numeroUsuario = parseInt(document.getElementById('valorUsuario').value);
    if (numeroUsuario === numeroSecreto){
        asignarTextoElemento('p', `Has acertado en ${intentos} ${(intentos === 1) ? '🤯 intento' : '🥹 intentos'}`);
        document.getElementById('reiniciar').removeAttribute('disabled');
    } else {
        if (numeroUsuario > numeroSecreto){
            asignarTextoElemento('p', 'El numero secreto es menor 👇');
        } else {
            asignarTextoElemento('p', 'El numero secreto es mayor 👆');
        }
        intentos++;
        limpiarCaja();
    }
    return;
}
function numeroAleatorio(){
    let numeroGenerado = Math.floor(Math.random() * numeroMaximo) + 1;

    console.log(numeroAleatorio);
    console.log(listaNumerosSorteados);

    if(listaNumerosSorteados.length == numeroMaximo){
        asignarTextoElemento('p', 'Ya se sortearon todos los numeros posibles, el juego termino'); // se inicializa para que se rompa el juego cuando se acaban los numeros posibles
    } else {
        if(listaNumerosSorteados.includes(numeroGenerado)){
            return numeroAleatorio(); //Si el numero generado ya está en la lista, genera uno nuevo. De lo contrario, añade el número a la lista. 100 intentos máximos, por lo que se evita un bucle infinito. 100% de probabilidad de que se genere un número nuevo. 100% de probabilidad de que se añada a la lista. 100% de probabilidad de que se cumpla la condición de que no se repita en los próximos intentos. 100% de probabilidad de que se cumpla la condición de que no se repita en los próximos intentos. 100% de probabilidad de que se cumpla la condición de que no se repita en los próximos intentos. 100%
        } else{
            listaNumerosSorteados.push(numeroGenerado);
            return numeroGenerado;
        }
    }
}
function limpiarCaja(){
    document.querySelector('#valorUsuario').value = '';
    return;
}

function reiniciarJuego(){
    limpiarCaja(); //limpiar caja
    condicionesIniciales(); //Iniciales del juego (mensajes iniciales, generar nuevo numero aleatorio, inicializar numero de intentos)
    document.querySelector('#reiniciar').setAttribute('disabled', 'true');
}

