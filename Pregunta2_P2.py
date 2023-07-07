"""
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas.
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


class Hija(Persona):
    def __init__(self):
        super().__init__()
        self.saldo = None
    def ingrese_saldo(self):
        self.saldo = int(input("Ingrese saldo: "))
    def transferencia(self, monto, destinatario):
        if self.saldo >= monto:
            self.saldo -= monto
            print("Transferencia exitosa, ahora tienes {} de saldo.".format(self.saldo-monto))
        else:
            print("Saldo insuficiente.")

persona_1 = Hija()
persona_1.ingresar_nombre_edad()
persona_1.ingrese_saldo()
monto = int(input("Ingrese el monto a transferir: "))
persona_destino = str(input("A quien deseas transferir: "))
persona_1.transferencia(monto, persona_destino)

