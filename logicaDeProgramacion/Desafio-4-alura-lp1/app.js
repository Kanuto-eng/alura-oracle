// Crea un programa que utilice console.log para mostrar un mensaje de bienvenida.

let mensajeBienvenida = " Hola 😘 bienvenido a nuestro programa";
console.log(mensajeBienvenida);

// Crea una variable llamada "nombre" y asígnale tu nombre. Luego, utiliza console.log para mostrar el mensaje "¡Hola, [tu nombre]!" en la consola del navegador.

let nombre = "Camilo 💕";
console.log(`Hola ${nombre}! Bienvenido a nuestro programa`);

// Crea una variable llamada "nombre" y asígnale tu nombre. Luego,utiliza alert para mostrar el mensaje "¡Hola, [tu nombre]!".

let nombre2 = "Camilo";
alert(`Hola ${nombre2}! `);

// Utiliza prompt y haz la siguiente pregunta: ¿Cuál es el lenguaje de programación que más te gusta?. Luego, almacena la respuesta en una variable y muestra la respuesta en la consola del navegador.

let lenguajeProgramacion = prompt("¿Cuál es el lenguaje de programación que más te gusta?");
console.log(`Has dicho que ${lenguajeProgramacion} es tu lenguaje de programación favorito.`);

// Crea una variable llamada "valor1" y otra llamada "valor2", asignándoles valores numéricos de tu elección. Luego, realiza la resta de estos dos valores y almacena el resultado en una tercera variable llamada "resultado". Utiliza console.log para mostrar el mensaje "La diferencia entre [valor1] y [valor2] es igual a [resultado]." en la consola.

let valor1 = 50;
let valor2 = 35;
let resultado = valor1 - valor2;
console.log(`La diferencia entre ${valor1} y ${valor2} es igual a ${resultado}.`);

// Pide al usuario que ingrese su edad con prompt. Con base en la edad ingresada, utiliza un if para verificar si la persona es mayor o menor de edad y muestra un mensaje apropiado en la consola.

let edad = parseInt(prompt("¿Cuál es tu edad por favor?"));

if (edad >= 18) {
    console.log("Genial eres mayor de edad.");
} else {
    console.log("algun dia creceras aun eres menor de edad.");
}

//  Crea una variable "numero" y solicita un valor con prompt. Luego, verifica si es positivo, negativo o cero utilizando un if-else y muestra el mensaje correspondiente.

let numero = parseInt(prompt("Por favor indicame un numero para saber si es positivo o negativo"));

if (numero > 0) {
    console.log(`${numero} es un número positivo.`);
} else if (numero < 0 ){
    console.log(`${numero} es un número negativo.`);
} else {
    console.log(`${numero} es cero`);
}

// Utiliza un bucle while para mostrar los números del 1 al 10 en la consola.

let numeros = 1

while (numeros <= 10) {
    console.log(numeros);
    numeros++;
}

// Crea una variable "nota" y asígnale un valor numérico. Utiliza un if-else para determinar si la nota es mayor o igual a 7 y muestra "Aprobado" o "Reprobado" en la consola.

let nota = parseInt(prompt("Digita la nota que sacaste en el curso"));

if (nota >= 7){
    console.log("El alumno aprobó el curso.");
} else {
    console.log("El alumno reprobó el curso.");
}

// Utiliza Math.random para generar cualquier número aleatorio y muestra ese número en la consola.

let random = Math.random();
console.log(random);

// Utiliza Math.random para generar un número entero entre 1 y 10 y muestra ese número en la consola.
function aleatorios( min, max){
    return Math.floor(Math.random() * (max - min + 1) + min);
}

let numeroEnteroAleatorio = aleatorios(1, 10);
console.log(numeroEnteroAleatorio);

// Utiliza Math.random para generar un número entero entre 1 y 1000 y muestra ese número en la consola.

let numeroEnteroAleatorio2 = aleatorios(1, 1000);
console.log(numeroEnteroAleatorio2);