# ---------------------------------------------------
# Programa: Conversión de temperatura Celsius a Fahrenheit
# Autor: Belgica Licto
# Asignatura: Programación
# Descripción:
# Este programa solicita al usuario una temperatura en grados
# Celsius, la convierte a grados Fahrenheit y muestra el resultado.
# En el programa se aplican tipos de datos, identificadores
# correctos y buenas prácticas de programación en Python.
# ---------------------------------------------------

# =========================
# ENTRADA DE DATOS
# =========================

# Dato tipo float: almacena la temperatura ingresada por el usuario
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# =========================
# PROCESO
# =========================

# Dato tipo float: resultado de la conversión
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Dato tipo boolean: verifica si la temperatura es alta
es_temperatura_alta = temperatura_fahrenheit > 86

# =========================
# SALIDA DE DATOS
# =========================

# Datos tipo string mostrados en pantalla
print("Temperatura en grados Celsius:", temperatura_celsius)
print("Temperatura en grados Fahrenheit:", temperatura_fahrenheit)

# Evaluación usando una estructura condicional
if es_temperatura_alta:
    print("La temperatura es alta.")
else:
    print("La temperatura no es alta.")
