//Crea una función que calcule el índice de masa corporal (IMC) de una persona a partir de su altura en metros y peso en kilogramos, que se recibirán como parámetros.
let altura=parseFloat(prompt('Ingrese su altura en metros:'));
let peso=parseFloat(prompt('Ingrese su peso en kilogramos:'));
let imc = 0;
function calcularIMC(peso, altura){
    imc = Number((peso / altura ** 2).toFixed(2)); // decimales arreglados para dos digitos dependiendoel numero
    if (imc <= 18.5){
        console.log(`Su IMC: ${imc} tiene peso bajo`);
    } else if (imc >= 18.6 && imc <= 24.9){
        console.log(`Su IMC: ${imc} tiene un peso normal`);
    } else if (imc >= 25 && imc <= 29.9){
        console.log(`Su IMC: ${imc} tiene sobre peso`);
    } else{
        console.log(`Su IMC: ${imc} tiene obesidad`);
    }
}
console.log(calcularIMC(peso, altura));

// Crea una función que calcule el valor del factorial de un número pasado como parámetro.
let numero = parseInt(prompt('Ingrese un numero para saber su factorial'));
function calcularFactorial(numero){
    let factorial = 1;
    for(let i = 1; i <= numero; i++){
        factorial *= i;
    }
    return factorial;
}
console.log(calcularFactorial(numero));

// Crea una función que convierta un valor en dólares, pasado como parámetro, y devuelva el valor equivalente en reales(moneda brasileña,si deseas puedes hacerlo con el valor del dólar en tu país). Para esto, considera la cotización del dólar igual a R$4,80.
let dolares = parseFloat(prompt('Ingrese el valor en dólares:'));
let cambioCop = 4.191;

function convertirDolaresCop(dolares){
    let COP = dolares * cambioCop;
    console.log(`El valor equivalente en pesos colombianos es: ${COP.toFixed(3)} COP`);
    return COP;
}
convertirDolaresCop(dolares);

// Crea una función que muestre en pantalla el área y el perímetro de una sala rectangular, utilizando la altura y la anchura que se proporcionarán como parámetros.
let alto = parseFloat(prompt('Ingrese la altura de la sala en metros:'));
let ancho = parseFloat(prompt('Ingrese la anchura de la sala en metros:'));
function calcularAreaPerimetro(alto, ancho){
    let area = alto * ancho;
    let perimetro = 2 * (alto + ancho);
    console.log(`El área de la sala es: ${area.toFixed(2)} m²`);
    console.log(`El perímetro de la sala es: ${perimetro.toFixed(2)} m`);
}
calcularAreaPerimetro(alto, ancho);

// Crea una función que muestre en pantalla el área y el perímetro de una sala circular, utilizando su radio que se proporcionará como parámetro. Considera Pi = 3,14.
let radio = parseFloat(prompt('Ingrese el radio de la sala en metros:'));
function calcularAreaPerimetroCirculo(radio){
    let area = Math.PI * radio ** 2;
    let perimetro = 2 * Math.PI * radio;
    console.log(`El área de la sala es: ${area.toFixed(2)} m²`);
    console.log(`El perímetro de la sala es: ${perimetro.toFixed(2)} m`);

}

// Crea una función que muestre en pantalla la tabla de multiplicar de un número dado como parámetro.
let numeroM = parseInt(prompt('Ingrese un número para saber tabla de multiplicar'));

function tablaMultiplicar(numeroM) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${numeroM} x ${i} = ${numeroM * i}`);
    }
    return;
}
tablaMultiplicar(numeroM);