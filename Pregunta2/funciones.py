import random
import math


def generar_lista_numeros(tamano):
    numeros = []
    for _ in range(tamano):
        numero = random.randint(1, 101)
        numeros.append(numero)
    return numeros


def leer_lista_notas():
    notas = []
    archivo_notas = open("notas.txt", "r")
    for linea in archivo_notas:
        if linea.strip().isdigit():
            notas.append(int(linea.strip()))
    archivo_notas.close()
    return notas


def calcular_raiz_cuadrada(numero):
    return round(math.sqrt(float(numero)), 3)
