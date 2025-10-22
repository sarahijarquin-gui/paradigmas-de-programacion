# Estructura de control de ciclo FOR
# Este codigo fue creado por
# aqui se anaden los nombres

nombres = ["ANGEL MAURICIO", "MARCO ANTONIO", "EDGAR DANIEL", "BETHZY ALEYDIZ", "FABIOLA MICHEL", 
"FRIDA VICTORIA", "ERNESTO YAHIR", "ANGEL YAEL", "AMBAR NAHOMI", "URIEL", "LUIS ENRIQUE", 
"BRAYAN ALEXANDER", "ERICK", "FERNANDA ABIGAIL", "ESTEFANI SARAHI", "YUMIKO JATZERY", 
"HANSEL DANIEL", "JULIO ALBERTO", "ENRIQUE UCIEL", "YOJAN JOEL", "PEDRO EDUARDO", 
"MIREYA YAMILE", "ALISON DAYANA", "PRISCILA", "SERGIO ALEXIS", "RICARDO", "SAMUEL JESHUA", 
"VANESSA ISABEL", "SARAHI VALERIA", "DAVID GERSSAYN", "JOSE ANGEL", "GABRIEL", 
"CHRISTIAN YUREM", "ARTURO AZAEL", "ARMANDO"]

# En esta parte se eligen los nombres con estas vocales
vocales = ("A", "E", "I", "O", "U")
inicio_vocal = 0  # en esta linea se inicia el contador

for nombre in nombres:  # la sentencia for recorre los nombres
    if nombre[0] in vocales:
        inicio_vocal += 1

print("Nombres que inician con vocal:", inicio_vocal)

# 2. Cuantos nombres tienen mas de 10 letras
mas_de_10 = 0
for nombre in nombres:
    if len(nombre.replace(" ", "")) > 10:
        mas_de_10 += 1

print("Nombres con mas de 10 caracteres (sin espacio):", mas_de_10)

# 3. Primeros 3 nombres en orden alfabetico
nombres_ordenados = sorted(nombres)
print("Primeros 3 nombres en orden alfabetico:")
for nombre in nombres_ordenados[:3]:
    print(nombre)

# 4. Buscar nombres que contienen la letra "Y"
con_y = []
for nombre in nombres:
    if "Y" in nombre:
        con_y.append(nombre)

print("Nombres que contienen la letra Y:")
for nombre in con_y:
    print(nombre)


# Estructura de control utilizando condicional if else
# Lista de calificaciones de estudiantes
calificaciones = [85, 60, 78, 45, 92, 55, 70, 100, 39, 68, 80, 59]

# 1. Clasificar cada calificacion usando if else
print("Clasificacion de cada calificacion:")
aprobados = 0
reprobados = 0

for cal in calificaciones:
    if cal >= 60:
        print(f"{cal}: Aprobado")
        aprobados += 1
    else:
        print(f"{cal}: Reprobado")
        reprobados += 1

# 2. Contar cuantos aprobaron y reprobaron
print("\nTotal de aprobados:", aprobados)
print("Total de reprobados:", reprobados)

# 3. Encontrar la calificacion mas alta y mas baja usando if else
maxima = calificaciones[0]
minima = calificaciones[0]

for cal in calificaciones:
    if cal > maxima:
        maxima = cal
    if cal < minima:
        minima = cal

print("\nLa calificacion mas alta es:", maxima)
print("La calificacion mas baja es:", minima)

# 4. Analizar si cada calificacion es par o impar usando if else
print("\nParidad de cada calificacion:")
for cal in calificaciones:
    if cal % 2 == 0:
        print(f"{cal} es par")
    else:
        print(f"{cal} es impar")


# Estructura de control de ciclo WHILE
# Solicitar al usuario la cantidad de datos a analizar
n = int(input("Cuantos datos deseas ingresar? "))

# Leer los datos
datos = []
contador = 0

while contador < n:
    valor = float(input(f"Ingrese el valor {contador + 1}: "))
    datos.append(valor)
    contador += 1

# Analisis con ciclo while
indice = 0
suma = 0
maximo = datos[0]
minimo = datos[0]
positivos = 0
negativos = 0
ceros = 0

while indice < n:
    valor = datos[indice]
    suma += valor

    if valor > maximo:
        maximo = valor
    if valor < minimo:
        minimo = valor

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
    else:
        ceros += 1

    indice += 1

# Resultados
promedio = suma / n
print("\nResultados del analisis:")
print("Datos ingresados:", datos)
print("Suma:", suma)
print("Promedio:", promedio)
print("Valor maximo:", maximo)
print("Valor minimo:", minimo)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)