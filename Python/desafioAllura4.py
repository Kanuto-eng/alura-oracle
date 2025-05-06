########### Entrenando la programación

# 1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().

listaGastosEmpresa = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
promedioGastos = sum(listaGastosEmpresa) / len(listaGastosEmpresa)
print(f"El promedio de gastos es: {promedioGastos:.2f}")

# 2 - Con los mismos datos de la pregunta anterior, determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.

listaGastosEmpresa = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
comprasSuperiores3000 = 0
for comprasSuperiores3000 in listaGastosEmpresa:
    if comprasSuperiores3000 > 3000:
        porcentajeComprasSuperiores3000 = (comprasSuperiores3000 / len(listaGastosEmpresa)) * 100
        
print(f"El promedio de compras superiores a 3000 es: {porcentajeComprasSuperiores3000:.2f}")

# 3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].

import random
print("Generando números aleatorios...")
print("Presione 1 para generar números aleatorios o 0 para no generar.")

numerosAleatorios = [random.randint(1, 100)]
generarAleatorios = int(input("Ingrese 1 o 0: "))

if generarAleatorios != 1 and generarAleatorios != 0:
    print("No se seleccionó ni 1 ni 0.")

elif generarAleatorios == 1:
    for i in range(11):
        numerosAleatorios.append(random.randint(1, 100))

    print(f"Lista de números aleatorios generados: {numerosAleatorios}")

else:
    print("No se generaron números aleatorios.")


# 4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.

print("Ordenador de números a la inversa de lo enviado...")
listaNumerosEnteros = []

for i in range(10):
    numero = int(input("Ingrese un número entero: "))
    listaNumerosEnteros.append(numero)

print(f"Lista de números enteros en orden inicial: {listaNumerosEnteros}")

listaNumerosEnteros.reverse()
print(f"Lista de números enteros en orden inverso: {listaNumerosEnteros}")

# 5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.

print("Generador de números primos...")
numero = int(input("Ingrese un número: "))
listaPrimos = []
for i in range(2, numero + 1):
    esPrimo = True
    for j in range(2, int(numero ** 0.5) + 1):
        if i % j == 0:
            esPrimo = False
            break
    if esPrimo:
        listaPrimos.append(i)
print(f"Lista de números primos entre 1 y {numero}: {listaPrimos}")

# 6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.

print("Validador de fechas...")

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
ano = int(input("Ingrese el año (use números negativos para a.C. y positivos para d.C.): "))

# Función para verificar si un año es bisiesto (solo válido para años d.C.)
def es_bisiesto(anio):
    return anio > 0 and ((anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0))

# Validar mes
if mes < 1 or mes > 12:
    print("Fecha inválida: mes fuera de rango.")
else:
    # Días máximos por mes (teniendo en cuenta si el año es bisiesto)
    dias_por_mes = {
        1: 31,
        2: 29 if es_bisiesto(ano) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if dia < 1 or dia > dias_por_mes[mes]:
        print("Fecha inválida: día fuera de rango.")
    else:
        era = "a.C." if ano < 0 else "d.C."
        print(f"Fecha válida: {dia}/{mes}/{abs(ano)} {era}")

########### Momento para los proyectos

# 7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

numeroBacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
porcentajeCrecimiento = []

# Calcular porcentaje de crecimiento diario a partir de los datos reales
for i in range(1, len(numeroBacterias)):
    muestra_anterior = numeroBacterias[i - 1]
    muestra_actual = numeroBacterias[i]
    crecimiento = 100 * (muestra_actual - muestra_anterior) / muestra_anterior
    porcentajeCrecimiento.append(crecimiento)

# Calcular el crecimiento promedio diario
promedio_crecimiento = sum(porcentajeCrecimiento) / len(porcentajeCrecimiento)

# Proyectar hasta completar 30 días
datos_completos = numeroBacterias.copy()
while len(datos_completos) < 30:
    anterior = datos_completos[-1]
    siguiente = anterior + anterior * (promedio_crecimiento / 100)
    datos_completos.append(siguiente)

# Mostrar resultados
print(f"Proyección del crecimiento de bacterias durante 30 días (con crecimiento promedio de {promedio_crecimiento:.2f}%):")
for i, cantidad in enumerate(datos_completos, start=1):
    print(f"Día {i}: {cantidad:.2f} bacterias")
    

# 8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. Luego, calcula y muestra la cantidad de productos dulces y amargos.

Ids = []
for i in range(10):
    id = int(input("Ingrese un ID: "))
    Ids.append(id)
    if id % 2 == 0:
        print(f"El producto con id {id:.0f} es dulce.")
    else:
        print(f"El producto con id {id} es amargo.")

print(f"Cantidad de productos dulces: {len([id for id in Ids if id % 2 == 0])}")
print(f"Cantidad de productos amargos: {len([id for id in Ids if id % 2 != 0])}")

# 9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D.

# Resultado del examen:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

print("Sistema de calificación de examen...")

# Respuestas correctas
print("Sistema de calificación de examen...")

# Respuestas correctas
resultadoExamen = {
    "01": "D",
    "02": "A",
    "03": "C",
    "04": "B",
    "05": "A",
    "06": "D",
    "07": "C",
    "08": "C",
    "09": "A",
    "10": "B"
}

# Listas para guardar resultados
respuestas_correctas = []
respuestas_incorrectas = []

print("Ingrese sus respuestas (A, B, C o D):")
puntuacion = 0

# Comparar respuestas del estudiante
for pregunta in resultadoExamen.keys():
    respuesta = input(f"Respuesta para la pregunta {pregunta}: ").strip().upper()
    
    if respuesta == resultadoExamen[pregunta]:
        puntuacion += 1
        respuestas_correctas.append((pregunta, respuesta))
    else:
        respuestas_incorrectas.append((pregunta, respuesta, resultadoExamen[pregunta]))

# Mostrar resultados
print("\n=== RESULTADOS ===")
print(f"Puntuación final: {puntuacion} de {len(resultadoExamen)}\n")

print("✅ Preguntas respondidas correctamente:")
for pregunta, respuesta in respuestas_correctas:
    print(f"Pregunta {pregunta}: respondiste '{respuesta}' ✔️")

print("\n❌ Preguntas respondidas incorrectamente:")
for pregunta, respuesta_estudiante, respuesta_correcta in respuestas_incorrectas:
    print(f"Pregunta {pregunta}: respondiste '{respuesta_estudiante}', era '{respuesta_correcta}'")

# 10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).

print("Sistema de análisis de temperatura...")
temperaturasMediasMeses = []
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
print("Ingrese las temperaturas medias de cada mes:")
for mes in meses:
    temperatura = float(input(f"Temperatura media de {mes}: "))
    temperaturasMediasMeses.append(temperatura)
    
promedioAnual = sum(temperaturasMediasMeses) / len(temperaturasMediasMeses)

mesesPorEncimaPromedio = [meses[i] for i in range(len(temperaturasMediasMeses)) if temperaturasMediasMeses[i] > promedioAnual]

print(f"Promedio anual de temperaturas: {promedioAnual:.2f}")
print(f"Meses con temperaturas por encima del promedio anual: {mesesPorEncimaPromedio}") 

# 11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:

# {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30} Escribe un código que calcule el total de ventas y el producto más vendido.

# Datos de ventas por producto
ventasProductos = {
    'Producto A': 300, 
    'Producto B': 80, 
    'Producto C': 60, 
    'Producto D': 200, 
    'Producto E': 250, 
    'Producto F': 30
}

# Calcular total de ventas
totalVentas = sum(ventasProductos.values())

# Identificar producto más vendido
productoMasVendido = max(ventasProductos, key=ventasProductos.get)
unidadesVendidas = ventasProductos[productoMasVendido]

# Mostrar resultados
print(f"Total de ventas: {totalVentas}")
print(f"Producto más vendido: {productoMasVendido} con {unidadesVendidas} unidades vendidas.")

# 12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:

# Tabla de votos de la marca
# Diseño 1 - 1334 votos
# Diseño 2 - 982 votos
# Diseño 3 - 1751 votos
# Diseño 4 - 210 votos
# Diseño 5 - 1811 votos

# Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.

votosMarca = {
    'Diseño 1': 1334,
    'Diseño 2': 982,
    'Diseño 3': 1751,
    'Diseño 4': 210,
    'Diseño 5': 1811
    }

for diseño, votos in votosMarca.items():
    porcentajeVotos = (votos / sum(votosMarca.values())) * 100
    print(f"{diseño} recibió {porcentajeVotos:.2f}% de los votos.")
    
print(f"El diseño ganador es: {max(votosMarca, key=votosMarca.get)} con {max(votosMarca.values())} votos.")


# 13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo. El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. La bonificación de cada empleado no puede ser inferior a 200. En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación de cada salario en el valor correspondiente. Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.

print("Sistema de bonificaciones...")
print("Bonificación de 10% de salario...")

# Diccionario con salarios y las bonificaciones iniciales (10% de salario)
bonificaciones = {
    1172: 117.20,
    1644: 164.40,
    2617: 261.70,
    5130: 513.00,
    5532: 553.20,
    6341: 634.10,
    6650: 665.00,
    7238: 723.80,
    7685: 768.50,
    7782: 778.20,
    7903: 790.30
}

# Actualizar bonificaciones para asegurar que no sean menores a 200
for salario in bonificaciones.keys():
    bonificacion = salario * 0.10   # Calcular bonificación (10% del salario)
    if bonificacion < 200:          # Asegurarse que la bonificación no sea menor a 200
        bonificacion = 200
    
    bonificaciones[salario] = bonificacion # Actualizar el diccionario con la bonificación final

# Imprimir bonificaciones de cada empleado
for salario, bonificacion in bonificaciones.items():
    print(f"El empleado con salario {salario} recibirá una bonificación de {bonificacion:.2f}.")

# Calcular el gasto total en bonificaciones
gasto_total = sum(bonificaciones.values())

# Calcular el número de empleados con bonificación mínima (200)
empleados_minima = len([b for b in bonificaciones.values() if b == 200])

# Obtener el valor máximo de bonificación
bonificacion_maxima = max(bonificaciones.values())

# Imprimir resultados finales
print(f"\nEl gasto total en bonificaciones es: {gasto_total:.2f}.")
print(f"El número de empleados que recibieron la bonificación mínima es: {empleados_minima}.")
print(f"El valor más alto de la bonificación proporcionada es: {bonificacion_maxima:.2f}.")


# 14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario. En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.

# {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

# Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica. Sugerencia: utiliza las funciones incorporadas sum() y len().

diversidadBiologica = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

areaConMayorDiversidad = ''
mayorDiversidad = 0

for area, especies in diversidadBiologica.items():
    promedioEspecies = sum(especies) / len(especies)
    print(f"Área {area} tiene un promedio de {promedioEspecies:.2f} especies.")
    
    if promedioEspecies > mayorDiversidad:
        mayorDiversidad = promedioEspecies
        areaConMayorDiversidad = area

print(f"\nEl área con mayor diversidad biológica es: {areaConMayorDiversidad} con un promedio de {mayorDiversidad:.2f} especies.")

# 15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa. Para ello, te proporcionaron los siguientes datos:

# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
# 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
# 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
# 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector, la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.

sectoresColaboradores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

# Calcular la media de edad de cada sector
edadesPorSector = {}
for sector, edades in sectoresColaboradores.items():
    mediaEdad = sum(edades) / len(edades)
    edadesPorSector[sector] = mediaEdad
    print(f"Media general de edad en {sector}: {mediaEdad:.2f} años.")
    print(f"Colaboradores en {sector} por encima de la media: {len([edad for edad in edades if edad > mediaEdad])} colaboradores.")

# Calcular la media general de edad entre todos los sectores
mediaGeneral = sum([edad for edades in sectoresColaboradores.values() for edad in edades]) / sum([len(edades) for edades in sectoresColaboradores.values()])
print(f"\nMedia general de edad entre todos los sectores: {mediaGeneral:.2f} años.")
# Calcular cuántas personas están por encima de la media general
mediaEdadGeneral = len([edad for edades in sectoresColaboradores.values() for edad in edades if edad > mediaGeneral])
print(f"Colaboradores por encima de la media general: {mediaEdadGeneral} colaboradores.")