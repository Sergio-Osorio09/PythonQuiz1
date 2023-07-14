"""
Funciones
"""

import random


def generar_lista_numeros():

    numeros = []
    for _ in range(10):
        numero = random.randint(1, 100)
        numeros.append(numero)
    return numeros


def eliminar_repetidos(lista):
    numeros_no_repetidos = list(set(lista))
    return numeros_no_repetidos


def ordenar_lista(numeros):
    numeros_ordenados_desc = sorted(numeros, reverse=True)
    numeros_ordenados_asc = sorted(numeros)
    return numeros_ordenados_desc, numeros_ordenados_asc


def encontrar_maximo(lista):
    maximo = max(lista)
    return maximo
