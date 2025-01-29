// Crea un contador que comience en 1 y vaya hasta 10 usando un bucle 'while'. Muestra cada número.

let contador = 1;

while (contador <= 10) {
  console.log(contador);
  contador++;
}

// Crea un contador que comience en 10 y vaya hasta 0 usando un bucle 'while'. Muestra cada número.

let contador2 = 10;

while (contador2 >= 0) {
  console.log(contador2);
  contador2--;
}

// Crea un programa de cuenta regresiva. Pide un número y cuenta desde 0 hasta ese número utilizando un bucle 'while' en la consola del navegador.

let cuentaRegresiva = prompt(" indicame un numero para iniciar la cuenta: " );

while (cuentaRegresiva >= 0) {
    console.log(cuentaRegresiva);
    cuentaRegresiva--;
}

// Crea un programa de cuenta progresiva. Pide un número y cuenta desde 0 hasta ese número utilizando un bucle 'while' en la consola del navegador.

let cuentaProgresiva = prompt(" indicame un numero para iniciar la cuenta: " );

while(cuentaProgresiva <= 100) {
    console.log(cuentaProgresiva);
    cuentaProgresiva++;
}