# Entrenando la programación

# 1 - Escribe un programa que solicite dos números enteros e imprima todos los números enteros entre ellos.

print("Imprimir números enteros entre dos números ingresados")
print("-----------------------------------------------------")
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num2 < num1:
    for i in range(num2 + 1, num1):
        print(i)
else:
    print("Los números son iguales, no hay números enteros entre ellos.")


# 2 - Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, respectivamente. Supón que la colonia A comienza con 4 elementos y B con 10.

print("Calcular días para que la colonia A supere a la colonia B")
print("-----------------------------------------------------")
bacteria_A = int(input("Ingrese la cantidad inicial de la colonia A: "))
bacteria_B = int(input("Ingrese la cantidad inicial de la colonia B: "))
tasaCrecimiento_A = 0.03
tasaCrecimiento_B = 0.015
dias = 0

if bacteria_A > bacteria_B:
    print("Las colonia de la bacteria A ya ha superado la colonia de la bacteria B.")
elif bacteria_A == bacteria_B:
    print("Las colonia de las bacterias A y B son iguales.")
else:
    while bacteria_A <= bacteria_B:
        bacteria_A += bacteria_A * tasaCrecimiento_A
        bacteria_B += bacteria_B * tasaCrecimiento_B
        dias += 1

print(f"Después de {dias} días, la colonia A superará a la colonia B.")

# 3 - Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, necesitamos verificar si las calificaciones son válidas. Por lo tanto, escribe un programa que recibirá calificaciones del 0 al 5 y verificará si son valores válidos. Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario ingrese un valor válido.

print("Verificar calificaciones válidas")
print("-----------------------------------------------------")
print("Ingrese 15 calificaciones validas del 0 al 15:")

for i in range(15):
    while True:
        calificacion = float(input(f"Ingrese la calificación {i}: "))
        if 0 <= calificacion <= 5:
            print(f"Calificación {i} válida: {calificacion}")
            break
        else:
            print("Calificación inválida. Debe estar entre 0 y 5. Intente nuevamente.")

print('Verificación completa. Todas las notas son válidas.')

# 4 - Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y calcule su promedio. La lectura debe detenerse al ingresar el valor -273°C.

print("Programa para calcular el promedio de temperaturas para finalizar digite (-273)")
print("-----------------------------------------------------")
temperaturas = float(input("Ingrese la temperatura en grados Celsius para saber su promedio: "))
contador = 0
suma_temperaturas = 0

while temperaturas != -273:
    suma_temperaturas += temperaturas
    contador += 1
    
    temperaturas = float(input("Ingrese la temperatura en grados Celsius para saber su promedio: "))

promedio = suma_temperaturas / contador
print(f"El promedio de las temperaturas ingresadas es: {promedio:.2f} grados Celsius.")



# 5 - Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.

print("Calcular el factorial de un número entero")
print("-----------------------------------------------------")

num = int(input("Ingrese un número entero para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"El factorial de {num} es: {factorial}")

# Momento de los proyectos

# 6 - Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 2, la tabla de multiplicar debe mostrarse en el siguiente formato:
# Tabla de multiplicar del 2: 2 x 1 = 2, 2 x 2 = 4, [...], 2 x 10 = 20

print("Programa para generar tabla de multiplicar")
print("-----------------------------------------------------")
numero = int(input("Ingrese un número entero para generar su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7 - Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.

print("Programa para verificar si un número es primo")
print("-----------------------------------------------------")
numero = int(input("Ingrese un número entero para verificar si es primo: "))

if numero <= 1:
    print(f"{numero} no es un número primo (los primos son mayores que 1).")
elif numero == 2 or numero == 3:
    print(f"{numero} es un número primo.")
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es un número primo.")
            break
        else:
            print(f"{numero} es un número primo.")
            break

# 8 - Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. La entrada de datos se detendrá al ingresar un número negativo.

print("Programa para la distribución de edades de pensionistas")
print("-----------------------------------------------------")

print("Ingrese las edades de los pensionistas (número negativo para finalizar):")
numero = int(input("Ingrese la edad: "))
contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0

while numero >= 0:
    if 0 <= numero <= 25:
        contador_0_25 += 1
    elif 26 <= numero <= 50:
        contador_26_50 += 1
    elif 51 <= numero <= 75:
        contador_51_75 += 1
    elif 76 <= numero <= 100:
        contador_76_100 += 1
    else:
        print("Edad fuera de rango. Debe estar entre 0 y 100.")
        
    
    numero = int(input("Ingrese la edad: "))

print(f"Distribución de edades:")
print(f"[0-25]: {contador_0_25} personas")
print(f"[26-50]: {contador_26_50} personas")
print(f"[51-75]: {contador_51_75} personas")
print(f"[76-100]: {contador_76_100} personas")

# 9 - En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:

# Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).

# También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).

# Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, los votos nulos y los votos en blanco. Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.

print("Programa para calcular el ganador de la elección")
print("-----------------------------------------------------")

print("Ingrese los votos de los empleados (1, 2, 3, 4 para candidatos; 5 para nulos; 6 para en blanco):")

total_votos = 20  # Total de empleados que votaron

# Inicializar contadores para cada candidato y votos nulos y en blanco
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0

votos_nulos = 0
votos_blancos = 0

# recopilar los votos de los empleados usando estructura for y while
for i in range(1, 21):
    voto = int(input(f"Voto del empleado {i}: "))
    while voto < 1 or voto > 6:
        print("Voto inválido. Debe ser entre 1 y 6.")
        voto = int(input(f"Voto del empleado {i}: "))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1 
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_blancos += 1
        
# Calcular el ganador de la elección
votos_candidatos = [candidato_1, candidato_2, candidato_3, candidato_4]
mayor = max(votos_candidatos)
ganador = votos_candidatos.index(mayor) + 1

# Calcular el porcentaje de votos nulos y en blanco
porcentaje_nulos = (votos_nulos / total_votos) * 100
porcentaje_blancos = (votos_blancos / total_votos) * 100

# Calcular el porcentaje de votos nulos y en blanco

print(f"Porcentaje de votos nulos: {porcentaje_nulos:.2f}%")
print(f"Porcentaje de votos en blanco: {porcentaje_blancos:.2f}%")
print("******************************************")
# numero total de votos
print(f"Distribución de los votos:")
print("******************************************")
print(f"[candidato 1]: {candidato_1} personas")
print(f"[candidato 2]: {candidato_2} personas")
print(f"[candidato 3]: {candidato_3} personas")
print(f"[candidato 4]: {candidato_4} personas")
print(f"[votos nulos]: {votos_nulos} personas")
print(f"[votos en blanco]: {votos_blancos} personas")
print("******************************************")
# mostrar el ganador
print(f"\nEl ganador de la elección es el candidato {ganador} con {mayor} votos.")
print("******************************************")