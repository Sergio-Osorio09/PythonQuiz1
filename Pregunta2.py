"""
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas.
"""
numeros = [2, 7, 8, 11, 72, 6.5, 99, 103.45, 1]
cubos = []
cuadrados = []

for i in numeros:
    cubo = i ** 3
    cubos.append(cubo)
for i in numeros:
    cuadrado = i ** 2
    cuadrados.append(cuadrado)

suma = cubos + cuadrados
suma.reverse()
print(suma)

