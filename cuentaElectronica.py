#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.  
#Implementa los siguientes métodos:
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.


class Cuenta:
    def __init__(self, titular, cantidad = 0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular: {}\nCantidad: {}".format(self.titular,self.cantidad))

    def ingresar(self,cantidad):
        if cantidad < 0:
            raise ValueError(" debe ingresar un valor numerico positivo")
        else:
            self.cantidad = self.cantidad + cantidad
            return "Operacion Exitosa"
    
    def retirar(self, cantidad):
        if cantidad < 0:
            raise ValueError(" debe ingresar un valor numerico positivo")
        else:
            self.cantidad = self.cantidad - cantidad
            return "Operacion Exitosa"

cuenta1 = Cuenta("Bruno") 
cuenta1.mostrar()
cuenta1.ingresar(155)
print(cuenta1.cantidad)
