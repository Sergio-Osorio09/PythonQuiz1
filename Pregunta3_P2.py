"""
3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos los
cuáles serán ingresado por consola.
- Deberá tener una función en el caso haya una división entre cero y
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingrese correctamente.
"""

def ingresar_datos():
    while True:
        try:
            dato1 = int(input("Ingrese el primer dato: "))
            dato2 = int(input("Ingrese el segundo dato: "))
            return dato1, dato2
        except ValueError:
            print("Error: Los datos ingresados deben ser números.")

def division():
    while True:
        try:
            dato1, dato2 = ingresar_datos()
            resultado = dato1 / dato2
            print("El resultado de la división es: {}".format(resultado))
            break
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
        except ValueError:
            print("Error: Los datos ingresados deben ser números.")

def evaluar_suma():
    while True:
        try:
            dato1, dato2 = ingresar_datos()
            suma = dato1 + dato2
            print("La suma de los datos es: {}".format(suma))
            if suma < 0:
                raise ValueError("Error: La suma es negativa.")
            break
        except Exception:
            print("Error")


division()
evaluar_suma()
