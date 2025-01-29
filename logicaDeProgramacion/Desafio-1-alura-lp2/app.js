// Cambia el contenido de la etiqueta h1 con document.querySelector y asigna el siguiente texto: "Hora del Desafío".
let etiqueta = document.querySelector('h1');
etiqueta.innerHTML = 'Hora del Desafío';

// Crea una función que muestre en la consola el mensaje "El botón fue clicado" siempre que se presione el botón "Console".
function btnClickConsole(){
    console.log('"El botón fue clicado"');
    alert('El botón fue clicado');
}

// Crea una función que se ejecute cuando se haga clic en el botón "prompt", preguntando el nombre de una ciudad de Brasil. Luego, muestra una alerta con el mensaje concatenando la respuesta con el texto: "Estuve en {ciudad} y me acordé de ti".
function btnClickPrompt(){
    let ciudad = prompt('Ingresa el nombre de una ciudad de brasil');
    alert(`Estuve en ${ciudad} y me acorde de ti!`);
}

// Crea una función que muestre una alerta con el mensaje: "Yo amo JS" siempre que se presione el botón "Alerta".
function btnClickAlert(){
    alert('Yo amo JS');
}

// Al hacer clic en el botón "suma", pide 2 números y muestra el resultado de la suma en una alerta.

function btnSuma(){
    alert('Indicame dos numeros para realizar una suma');
    let num1 = parseInt(prompt('Ingresa el primer número'));
    let num2 = parseInt(prompt('Ingresa el segundo número'));
    alert(`La suma de ${num1} y ${num2} es ${num1 + num2}`);
}