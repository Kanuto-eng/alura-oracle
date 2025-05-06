# Desafío Allura
# Recopilación y muestra de datos

# 1 - Crea un programa que solicite al usuario que escriba su nombre y luego imprima "Hola, [nombre]."

nombrePunto1= input("Escribe tu nombre: ")

print(f"Hola, {nombrePunto1}.")
print("==========================")

# 2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y luego imprima "Hola, [nombre], tienes [edad] años."

nombrePunto2 = input("Escribe tu nombre: ")
edadPunto2 = int(input("Escribe tu edad: "))
print(f"Hola, {nombrePunto2}, tienes {edadPunto2} años.")
print("==========================")

# 3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."

nombrePunto3 = input("Escribe tu nombre: ")
edadPunto3 = int(input("Escribe tu edad: "))
alturaPunto3 = float(input("Escribe tu altura: "))
print(f"Hola, {nombrePunto1}, tienes {edadPunto3} años, y mides {alturaPunto3} metros.")
print("==========================")

# Calculadora con operadores

# 4 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la suma de ambos valores.

print("Suma de dos numeros")
numeroPunto4  = int(input("Escribe tu primer numero: "))
numero2Punto4 = int(input("Escribe tu segundo numero: "))
sumaPunto4 = numeroPunto4 + numero2Punto4
print(f"La suma de {numeroPunto4} y {numero2Punto4} es: {sumaPunto4}")
print("La suma de " + str(numeroPunto4) + " y " + str(numero2Punto4) + " es: " + str(sumaPunto4))
print("==========================")

# 5 - Crea un programa que solicite tres valores numéricos al usuario y luego imprima la suma de los tres valores.

print("Suma de tres numeros")
numeroPunto5  = int(input("Escribe tu primer numero: "))
numero2Punto5 = int(input("Escribe tu segundo numero: "))
numero3Punto5 = int(input("Escribe tu tercer numero: "))
sumaPunto5 = numeroPunto5 + numero2Punto5 + numero3Punto5
print(f"La suma de {numeroPunto5}, {numero2Punto4} y {numero3Punto5} es: {sumaPunto5}")
print("==========================")

# 6 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la resta del primero menos el segundo valor.

print("Resta de dos numeros")
numeroPunto6  = int(input("Escribe tu primer numero: "))
numero2Punto6 = int(input("Escribe tu segundo numero: "))
restaPunto6 = numeroPunto6 - numero2Punto6
print(f"La resta de {numeroPunto6} y {numero2Punto6} es: {restaPunto6}")
print("==========================")

# 7 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la multiplicación de los dos valores.

print("Multiplicacion de dos numeros")
numeroPunto7  = int(input("Escribe tu primer numero: "))
numero2Punto7 = int(input("Escribe tu segundo numero: "))
multiplicacionPunto7 = numeroPunto7 * numero2Punto7
print(f"La multiplicacion de {numeroPunto7} y {numero2Punto7} es: {multiplicacionPunto7}")
print("==========================")

# 8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

print("Division de dos numeros")
numerador  = int(input("Escribe tu primer numero: "))
denominador = int(input("Escribe tu segundo numero: "))
divisionPunto8 = numerador / denominador
if denominador != 0:
    print(f"La division de {numerador} y {denominador} es: {divisionPunto8}")
else:
    print("El denominador no puede ser 0.")
print("==========================")

# 9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, y realice la exponenciación entre estos dos valores.

print("Potencia de dos numeros")
operador1  = int(input("Escribe tu primer numero: "))
potencia = int(input("Escoja la potencia: "))
exponenciacionPunto8 = operador1 ** potencia
print(f"El numero {operador1} con una potencia a la {potencia} es: {exponenciacionPunto8}")
print("==========================")

# 10 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entera entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

print("Division de dos numeros")
numeradorPunto10 = int(input("Escribe tu primer numero: "))
denominadorPunto10 = int(input("Escribe tu segundo numero: "))
divisionPunto10 = numeradorPunto10 / denominadorPunto10
if denominadorPunto10 != 0:
    print(f"La division de {numeradorPunto10} y {denominadorPunto10} es: {divisionPunto10}")
else:
    print("El denominador no puede ser 0.")
print("==========================")

# 11 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y devuelva el resto de la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

print("Resto de dos numeros")
numeradorPunto11  = int(input("Escribe tu primer numero: "))
denominadorPunto11 = int(input("Escribe tu segundo numero: "))
restoPunto11= numeradorPunto11 % denominadorPunto11
if denominadorPunto11 != 0:
    print(f"El resto de la division de {numeradorPunto11} y {denominadorPunto11} es: {restoPunto11}")
else:
    print("El denominador no puede ser 0.")
print("==========================")

# 12 - Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.

print("Promedio de tres notas")
nota1 = float(input("Escribe tu primera nota: "))
nota2 = float(input("Escribe tu segunda nota: "))   
nota3 = float(input("Escribe tu tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas es: {promedio}")
print("==========================")

# 13 - Crea un código que calcule e imprima el promedio ponderado de los números 5, 12, 20 y 15 con pesos respectivamente iguales a 1, 2, 3 y 4.

print("Promedio ponderado")
valores = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]
suma_productos = sum(valor * peso for valor, peso in zip(valores, pesos))
suma_pesos = sum(pesos)
promedio_ponderado = suma_productos / suma_pesos
print(f"El promedio ponderado es: {promedio_ponderado:.2f}")
print("==========================")

# Editando textos

# 14 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase en pantalla.

frase = "Hola, soy un programa de Python y puto el que lo lea."
print(frase)
print("==========================")

# 15 - Crea un código que solicite una frase y luego imprima la frase en pantalla.

frasePantalla = input("Escribe una frase: ")
print(frasePantalla)
print("==========================")

# 16 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.

frasePantalla1 = input("Escribe una frase: ")
print(frasePantalla1.upper())
print("==========================")

# 17 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.

frasePantalla2 = input("Escribe una frase: ")
print(frasePantalla2.lower())
print("==========================")

# 18 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase sin espacios en blanco al principio y al final.

frase1 = "  Hola, soy un texto y tengo espacios y puto el que lo lea. " 
print(frase1.strip())
print("==========================")

# 19 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final.

frase2 = input("Escribe una frase: ")
print(frase2.strip())
print("==========================")

# 20 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final, además de convertirla a minúsculas.

print("Frase en minusculas y sin espacios")
frase3 = input("Escribe una frase en mayusculas o combnacion de minuscula y mayuscula: ")
print(frase3.strip().lower())
print("==========================")

# 21 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".

print("Frase que reemplaza las vocales e por f")
frase4 = input("Escribe una frase: ")
print(frase4.lower().replace("e", "f"))
print("==========================")

# 22 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".

print("Frase que reemplaza las vocales a por @")
frase5 = input("Escribe una frase: ")
print(frase5.lower().replace("a", "@"))
print("==========================")

# 23 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".

print("Frase que reemplaza las consonantes s por $")
frase6 = input("Escribe una frase: ")
print(frase6.lower().replace("s", "$"))
print("==========================")
