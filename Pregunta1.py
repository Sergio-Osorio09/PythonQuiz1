"""
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los trabadores
localizándolos por la posición en la lista.
"""
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
print(type(nombre))
print(type(edad))
print("Hola,{} , su edad es {}".format(nombre, edad))

trabajadores = []
edades = []
trabajador_1 = str(input("Ingrese el nombre del trabajador 1: "))
trabajador_2 = str(input("Ingrese el nombre del trabajador 2: "))
trabajadores.append(trabajador_1)
trabajadores.append(trabajador_2)
print("La lista de trabajadores es: {}".format(trabajadores))
edad_1 = int(input("Ingrese edad de trabajador 1: "))
edad_2 = int(input("Ingrese edad de trabajador 2: "))
edades.append(edad_1)
edades.append(edad_2)
edades.append(edad_1 + edad_2)
print("{} tiene {}, {} tiene {} y la suma de sus edades es {}, ".format(trabajadores[0], edades[0], trabajadores[1],
                                                                        edades[1], edades[2]))
