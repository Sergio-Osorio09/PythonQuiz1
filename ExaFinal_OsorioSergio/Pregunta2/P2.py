"""
Pregunta 2
"""

import funciones


def crear_archivo_notas():
    archivo_notas = open("notas.txt", "w")
    archivo_notas.close()
    print("El archivo 'notas.txt' ha sido creado exitosamente.")


def escribir_lista_notas(tamano):
    try:
        archivo_notas = open("notas.txt", "a")
        notas = funciones.generar_lista_numeros(tamano)
        archivo_notas.write("Lista de notas:\n")
        for nota in notas:
            archivo_notas.write(str(nota) + "\n")
        archivo_notas.write("\n")
        archivo_notas.close()
        print("La lista de notas ha sido escrita en el archivo 'notas.txt'.")
    except TypeError:
        print("Error al escribir la lista de notas en el archivo 'notas.txt'.")


def calcular_raiz_cuadrada_notas():
    try:
        archivo_notas = open("notas.txt", "a")
        notas = funciones.leer_lista_notas()
        archivo_notas.write("Raiz cuadrada de las notas:\n")
        for nota in notas:
            raiz = funciones.calcular_raiz_cuadrada(nota)
            archivo_notas.write(str(raiz) + "\n")
        archivo_notas.write("\n")
        archivo_notas.close()
        print("La raiz cuadrada de las notas ha "
              "sido escrita en el archivo 'notas.txt'.")
    except TypeError:
        print("Error al calcular la raíz cuadrada de "
              "las notas y escribirla en el archivo 'notas.txt'.")


crear_archivo_notas()

tamano_lista = int(input("Ingrese el tamaño de la lista de notas: "))
escribir_lista_notas(tamano_lista)

calcular_raiz_cuadrada_notas()
