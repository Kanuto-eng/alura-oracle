// Crea una lista vacía llamada "listaGenerica".
let listaGenerica = [];

// Crea una lista de lenguajes de programación llamada "lenguagesDeProgramacion con los siguientes elementos: 'JavaScript', 'C', 'C++', 'Kotlin' y 'Python'.

let lenguajesDeProgramacion = [ 'JavaScript', 'C', 'C++', 'Kotlin', 'Python'];

// Agrega a la lista "lenguagesDeProgramacion los siguientes elementos: 'Java', 'Ruby' y 'GoLang'.

lenguajesDeProgramacion.push('Java', 'Ruby','GoLang');

// Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion.

function mostrarLenguajesDeProgramacion() {
  console.log(lenguajesDeProgramacion);
}
mostrarLenguajesDeProgramacion();

// Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion en orden inverso.

function mostrarLenguajesDeProgramacionEnOrdenInverso() {
  console.log(lenguajesDeProgramacion.reverse());
}
mostrarLenguajesDeProgramacionEnOrdenInverso();

// Crea una función que calcule el promedio de los elementos en una lista de números.
let listaNumeros = [];
let nota1 = parseFloat(prompt("Ingrese la primer nota"));
let nota2 = parseFloat(prompt("Ingrese la segunda nota"));
let nota3 = parseFloat(prompt("Ingrese la tercera nota"));
let nota4 = parseFloat(prompt("Ingrese la cuarta nota"));
let nota5 = parseFloat(prompt("Ingrese la quinta nota"));

listaNumeros.push(nota1, nota2, nota3, nota4, nota5);

console.log(listaNumeros);
function calcularPromedio(listaNumeros){
    let totalLista = 0;
    for (let i = 0; i < listaNumeros.length; i++) {
      totalLista += listaNumeros[i];
    }
    return totalLista / listaNumeros.length;
}

console.log("El promedio de las notas es: " + calcularPromedio(listaNumeros));

// Crea una función que muestre en la consola el número más grande y el número más pequeño en una lista.
let listaNumeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
function numeroMaximoMinimo(listaNumeros2) {
  let maximo = listaNumeros2[0];
  let minimo = listaNumeros2[0];
  for (let i = 0; i < listaNumeros2.length; i++) {
    if (listaNumeros2[i] > maximo) {
      maximo = listaNumeros2[i];
    } else if (listaNumeros2[i] < minimo) {
      minimo = listaNumeros2[i];
    }
  }
  console.log(`El Número máximo es: ${maximo}` );
  console.log(`El Número mínimo es: ${minimo}` );
}
numeroMaximoMinimo(listaNumeros2);

// Crea una función que devuelva la suma de todos los elementos en una lista.
function sumarElementos(listaNumeros2) {
  let suma = 0;
  for (let i = 0; i < listaNumeros2.length; i++) {
    suma += listaNumeros2[i];
  }
  return suma;
}

console.log("La suma de todos los elementos es: " + sumarElementos(listaNumeros2));

// Crea una función que devuelva la posición en la lista donde se encuentra un elemento pasado como parámetro, o -1 si no existe en la lista.

let elemento = parseInt(prompt("Ingrese el numero que desea buscar"))
function buscarElemento(listaNumeros2, elemento) {
  for(let i = 0; i < listaNumeros2.length; i++){
    if(listaNumeros2[i] === elemento){
      return console.log(`El elemento ${elemento} se encuentra en la posición ${i}`);
    }
  } return console.log(`(-1) El elemento ${elemento} no existe en la lista`);
}
console.log(buscarElemento(listaNumeros2, elemento));

// Crea una función que reciba dos listas de números del mismo tamaño y devuelva una nueva lista con la suma de los elementos uno a uno.

let listaNumeros3 = [1, 2, 3, 4, 5];
let listaNumeros4 = [6, 7, 8, 9, 10];
function sumaListas(listaNumeros3, listaNumeros4) {
  if (listaNumeros3.length !== listaNumeros4.length) {
    console.log("Las listas deben tener el mismo tamaño");
    return [];
  }

  let listaSuma = [];
  for (let i = 0; i < listaNumeros3.length; i++) {
      listaSuma.push(listaNumeros3[i] + listaNumeros4[i]);
    }
    return listaSuma;
}

console.log(sumaListas(listaNumeros3, listaNumeros4));

// Crea una función que reciba una lista de números y devuelva una nueva lista con el cuadrado de cada número.

let listaNumeros5 = [6, 7, 8, 9, 10];
function cuadradoListaNumeros(listaNumeros5){
  let listaCuadrados = [];
  for(let i = 0; i < listaNumeros5.length; i++){
    listaCuadrados.push(Math.pow(listaNumeros5[i], 2));
  }
  return listaCuadrados;
}
console.log(cuadradoListaNumeros(listaNumeros5));