# Entrenando la programación

#  1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.

print("Programa para encontrar el número mayor entre dos números.")
print("ingresa dos numeros: ")
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
if num1 > num2:
    print("el numero mayor es: ", num1)
elif num1 < num2:
    print("el numero mayor es: ", num2)
else:
    print("los numeros son iguales")

#  2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).

print("Programa para determinar el crecimiento o disminución de la producción de una empresa.")
print("ingresa el porcentaje de crecimiento de la empresa: ")
porcentaje = float(input("ingrese el valor del porcentaje: "))
if porcentaje > 0:
    print(f"Crecimiento: La producción aumentó un {porcentaje:.2f}%. ¡Buen trabajo!")
elif porcentaje < 0:
    print(f"Disminución: La producción bajó un {abs(porcentaje):.2f}%. Es importante revisar las causas.")
else:
    print("Estabilidad: No hubo cambios en la producción.")
    
#  3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.

print("Este programa permite identificar si una letra es vocal o consonante.")
letra = input("Ingrese una letra: ").lower()
if len(letra) != 1 or not letra.isalpha():
    print("Error: Debe ingresar solo una letra.")
elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f"La letra '{letra}' es una vocal.")
else:
    print(f"La letra '{letra}' es una consonante.")

#  4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.

print("Programa para encontrar el precio más alto y más bajo de un automóvil en 3 años.")
print("ingresa los precios de los tres años: ")
precio1 = float(input("precio año 1: "))
precio2 = float(input("precio año 2: "))
precio3 = float(input("precio año 3: "))
#********************llamado de print dentro de condicional***************************
if precio1 > precio2 and precio1 > precio3:
    print("el precio más alto es: ", precio1)
elif precio2 > precio1 and precio2 > precio3:
    print("el precio más alto es: ", precio2)
else:
    print("el precio más alto es: ", precio3)
#********************llamado de print fuera de condicional asignando variables dentro de los condicionales***************************
if precio1 < precio2 and precio1 < precio3:
    precioMasBajo = precio1
elif precio2 < precio1 and precio2 < precio3:
    precioMasBajo = precio2
else:
    precioMasBajo = precio3
    
print("el precio más bajo es: ", precioMasBajo)


#  5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.

print("Programa para encontrar el producto más barato entre tres productos.")
print("ingresa los precios de los tres productos: ")
precioProducto1 = float(input("precio producto 1: "))
precioProducto2 = float(input("precio producto 2: "))
precioProducto3 = float(input("precio producto 3: "))
if precioProducto1 < precioProducto2 and precioProducto1 < precioProducto3:
    print("el producto más barato es: ", precioProducto1)
elif precioProducto2 < precioProducto1 and precioProducto2 < precioProducto3:
    print("el producto más barato es: ", precioProducto2)
else:
    print("el producto más barato es: ", precioProducto3)


#  6 - Escribe un programa que lea tres números y los muestre en orden descendente.

print("Programa para mostrar tres números en orden descendente.")
print("ingresa tres numeros: ")
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
num3 = int(input("numero 3: "))
mayor = medio = menor = 0

#***********numero mayor*************
if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
else:
    mayor = num3
#***********numero medio*************    
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3
#***********numero menor*************   
if (num1 != mayor and num1 != menor):
    medio = num1
elif (num2 != mayor and num2 != menor):
    medio = num2
else:
    medio = num3

print("el mayor es: ", mayor , "\nel medio es: ", medio , "\nel menor es: ", menor)

#  7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.

print("Programa para saludar según el turno de estudio.")
print("ingresa el turno de estudio: ")
print("opciones: mañana, tarde o noche")
turno = input("ingrese el turno: ").lower()
if turno == "mañana":
    print("¡Buenos Días!")
elif turno == "tarde":
    print("¡Buenas Tardes!")
elif turno == "noche":
    print("¡Buenas Noches!")
else:
    print("Valor Inválido!") 

#  8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).

print("Programa para determinar si un número es par o impar.")
print("ingresa un numero entero: ")
num = int(input("numero: "))
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")

#  9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.

print("Programa para determinar si un número es par o impar.")
print("ingresa un numero: ")
num = float(input("numero: "))
if num % 1 == 0:
    print(f"El número {num:.0f} es entero.")
else:
    print(f"El número {num:.1f} es decimal.")


#  Momento de los proyectos

#  10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.

print("Programa para realizar operaciones matematicas.")
print("seleccione la opcion que desea: suma, resta, multiplicacion, division")
operacion = input("ingrese la operacion: ").lower()
#*********************operaciones matematicas***************************
if operacion == "suma":
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    resultado = num1 + num2
elif operacion == "resta":
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    resultado = num1 - num2
elif operacion == "multiplicacion": 
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    resultado = num1 * num2
elif operacion == "division":
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2

#*********************resultado par/impar***************************
if resultado % 2 == 0:
    print(f"El número {resultado:.0f} es par.")
else:
    print(f"El número {resultado} es impar.")
    
#*********************resultado entero o decimal***************************    
if resultado % 1 == 0:
    print(f"El número {resultado:.0f} es entero.")
else:
    print(f"El número {resultado:.1f} es decimal.")
    
#*********************resultado positivo o negativo***************************
if resultado > 0:
    print(f"El número {resultado:.0f} es positivo.")
elif resultado < 0:
    print(f"El número {resultado:.1f} es negativo.")


#  11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:
#  Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
#  Triángulo Equilátero: tres lados iguales;
#  Triángulo Isósceles: dos lados iguales;
#  Triángulo Escaleno: tres lados diferentes.

print("Programa para determinar el tipo de triángulo.")
print("ingresa los lados del triángulo: ")
lado1= float(input("lado 1: "))
lado2= float(input("lado 2: "))
lado3= float(input("lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 and lado1 == lado3:
        print("Triángulo Equilátero: tres lados iguales")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triángulo Isósceles: dos lados iguales.")
    else:
        print("Triángulo Escaleno: tres lados diferentes.")  
else:
    print("Los valores ingresados no forman un triángulo.")  

#  12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:
#  El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
#  El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.

print("Programa para calcular el valor a pagar por combustible.")
print("ingresa la cantidad de litros vendidos: ")
litros = float(input("litros: "))
tipoCombustible= input("tipo de combustible (E para etanol y D para diésel): ").upper()
precioEtanol = 1.70     # precio por litro de etanol
precioDiesel = 2.00    # precio por litro de diésel
descuentoEtanol = 0.02 # descuento por litro hasta 15 litros
descuentoEtanolMayor = 0.04 # descuento por litro mayor a 15 litros
descuentoDiesel = 0.03  # descuento por litro hasta 15 litros
descuentoDieselMayor = 0.05 # descuento por litro mayor a 15 litros

if tipoCombustible == "E":
    if litros <= 15:
        sinDescuento= precioEtanol * litros
        descuento = precioEtanol * litros * descuentoEtanol
    elif litros > 15:
        sinDescuento= precioEtanol * litros
        descuento = precioEtanol * litros * descuentoEtanolMayor
    valorPagar = (precioEtanol * litros) - descuento
    print(f"El valor a pagar por {litros:.2f} litros de etanol sin descuento es de: {sinDescuento:.2f}, y paga: R$ {valorPagar:.2f} por el descuento")
elif tipoCombustible == "D":   
    if litros <= 15:
        sinDescuento= precioDiesel * litros
        descuento = precioDiesel * litros * descuentoDiesel
    elif litros > 15:
        sinDescuento= precioDiesel * litros
        descuento = precioDiesel * litros * descuentoDieselMayor
    valorPagar = (precioEtanol * litros) - descuento
    print(f"El valor a pagar por {litros:.2f} litros de diesel sin descuento es de: {sinDescuento:.2f}, y paga: R$ {valorPagar:.2f} por el descuento")
else:
    print("Error: Tipo de combustible no válido. Ingrese 'E' para etanol o 'D' para diésel.")


#  13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:
#  Para una variación superior al 20%: bonificación para el equipo de ventas.
#  Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
#  Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
#  Para bonificaciones inferiores al -10%: recorte de gastos.

print("Programa para analizar datos de ventas anuales.")
print("ingresa la cantidad de ventas del año 2022: ")
ventas2022 = int(input("ventas 2022: "))
ventas2023 = int(input("ventas 2023: "))
#*********************calculo de variacion porcentual***************************
variacion = ((ventas2023 - ventas2022) / ventas2022) * 100
print(f"Variación porcentual: {variacion:.2f}%")
if variacion > 20:
    print("Bonificación para el equipo de ventas.")
elif variacion >= 2  and variacion <= 20:
    print("Pequeña bonificación para el equipo de ventas.")
elif variacion >= -10 and variacion <= 2:
    print("Planificación de políticas de incentivo a las ventas.")
elif variacion < -10:
    print("Recorte de gastos.")