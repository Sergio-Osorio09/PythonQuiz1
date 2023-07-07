"""
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
"""
import datetime

class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.nacionalidad = "Peruana"

    def ingresar_nombre_edad(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

        ahora = datetime.datetime.now()
        fecha_registro = ahora.strftime("%Y-%m-%d %H:%M:%S")
        fecha, hora = fecha_registro.split(" ")
        print("Fecha de registro:", fecha, "Hora:", hora)

    def cumple(self):
        self.edad = self.edad + 1
        print("{} Feliz Cumpleaños # {}".format(self.nombre, self.edad))

persona_0 = Persona()
persona_0.ingresar_nombre_edad()
persona_0.cumple()
persona_0.cumple()
