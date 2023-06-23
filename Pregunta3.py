"""
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario.
"""
datos = {"nombre": "", "apellido": "", "edad": "", "dni": ""}

datos["nombre"] = str(input("Ingrese su nombre: ")).upper()
datos["apellido"] = str(input("Ingrese su apellido: ")).upper()
datos["edad"] = int(input("Ingrese su edad: "))
datos["dni"] = str(input("Ingrese su dni: "))

values = datos.values()
print(values)

datos["profesion"] = str(input("Ingrese su profesion: "))

del datos["dni"]
print("El nuevo diccionario es: {}".format(datos))