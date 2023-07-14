"""
Pregunta 1
"""

from ExaFinal_OsorioSergio.Pregunta1.Funcionalidades import \
    generar_lista_numeros,\
    eliminar_repetidos, ordenar_lista, \
    encontrar_maximo

numeros_aleatorios = generar_lista_numeros()
print("-------Lista de números aleatorios:-----------------------")
print(numeros_aleatorios)

numeros_no_repetidos = eliminar_repetidos(numeros_aleatorios)
print("\n-------Lista de números no repetidos:---------------------")
print(numeros_no_repetidos)


numeros_descendentes, numeros_ascendentes = ordenar_lista(numeros_no_repetidos)
print("\n-------Lista de números ordenados de mayor a menor:-------")
print(numeros_descendentes)
print("\n-------Lista de números ordenados de menor a mayor:-------")
print(numeros_ascendentes)

maximo_numero = encontrar_maximo(numeros_no_repetidos)
print("\n-------El número máximo de la lista es: {} ---------------"
      .format(maximo_numero))
