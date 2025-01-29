// Crear una función que muestre "¡Hola, mundo!" en la consola.
function saludo(){
    alert('Hola, 🌎!');
}
saludo();

// Crear una función que reciba un nombre como parámetro y muestre "¡Hola, [nombre]!" en la consola.
let nombre1 = prompt(" Ingrese un nombre por favor:");
function nombre(nombre){
    let nombreHTML = document.querySelector(nombre);
    console.log(`😎 Hola, ${nombre}!`);
    return;

}
nombre(nombre1);

// Crear una función que reciba un número como parámetro y devuelva el doble de ese número.
alert("Numero Doble");
let numero_1 = parseInt(prompt(" Ingrese un numero por favor: "));
function numeroDoble(numero){
     let doble = numero * 2;
     console.log(` El doble de su numero ${numero} es: ${doble}`);
     return;
}
numeroDoble(numero_1);

//
alert("Numero Promedio");
let numero1 = parseInt(prompt(" Ingrese el primer numero por favor: "));
let numero2 = parseInt(prompt(" Ingrese el segundo numero por favor: "));
let numero3 = parseInt(prompt(" Ingrese el tercer numero por favor: "));
function promedio(numero1, numero2, numero3){
    let prome = (numero1 + numero2 + numero3) / 3;
    console.log(` El promedio de los tres numeros es: ${prome}`);
    return;
}
promedio(numero1, numero2, numero3);

// Crear una función que reciba dos números como parámetros y devuelva el mayor de ellos.

alert("Numero Mayor y Menor");
let num1 = parseInt(prompt(" Ingrese el primer numero por favor: "));
let num2 = parseInt(prompt(" Ingrese el segundo numero por favor: "));
function numeroMayor(num1, num2){
    let numeroMayor;
    if(num1 > num2){
        numeroMayor = num1;
    } else if(num1 < num2){
        numeroMayor = num2;
        console.log(`El numero mayor es: ${numeroMayor}`);
    } else {
        numeroMayor = "Los numeros son iguales";
    }
    console.log(`${numeroMayor}`);
    return;
}
numeroMayor(num1, num2);

// Crear una función que reciba un número como parámetro y devuelva el resultado de multiplicar ese número por sí mismo.

alert("Numero Multiplicado por si Mismo");
let num = parseInt(prompt(" Ingrese el primer numero por favor: "));

function Multiplicacion(num){
    let multiplicado = num * num;
    console.log(` El resultado de multiplicar el numero ${num} por si mismo es: ${multiplicado}`);
    return;
}
Multiplicacion(num);
