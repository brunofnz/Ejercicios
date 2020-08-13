#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.  
#Implementa los siguientes métodos:
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de lo que definas al resolver el problema Cuenta Electrónica. 

#Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:

#En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

#Además la retirada de dinero sólo se podrá hacer si el titular es válido.

#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

#Piensa los métodos heredados de la clase madre que hay que reescribir.

from datetime import date
from datetime import datetime

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

class CuentaJoven(Cuenta):
    def __init__(self,titular,cantidad,bonificacion,edad):
        Cuenta.__init__(self,titular,cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def esTitularValido():
        pass

    def mostrar():
        pass


 # -*- coding: utf-8 -* 
# Importamos el objeto 'date' para manejar las fechas: from datetime import date 
 
def calcular_edad(nacimiento): 
    """ 
       Calcula la edad exacta de la persona tomando en cuenta      
      día, mes y año actual y mes, día y año de nacimiento. 
    """ 
   # Obtenemos la fecha de hoy:   hoy = date.today() 
   # Sustituimos el año de nacimiento por el actual:      
    try: 
        cumpleanios = nacimiento.replace(year=hoy.year) 
   # En caso de que la fecha de nacimiento es 29 de 
   # febrero y el año actual no sea bisiesto: 
    except ValueError: 
       # Le restamos uno al día de nacimiento para que quede en 28:       
        cumpleanios = nacimiento.replace(year=hoy.year, day=nacimiento.day - 1) 
   # Cálculo final: 
    if cumpleanios > hoy:          
        return hoy.year - nacimiento.year - 1 
    else: 
        return hoy.year - nacimiento.year 

def main(): 
    """Muestra un ejemplo.""" 
    dia, mes, anio = [int(v) for v in "31/03/1990".split("/")] 
    nacimiento = date(anio, mes, dia) 
    print(calcular_edad(nacimiento))

main()  









"""hoy = datetime.now()
dia = hoy.day
mes = hoy.month
anio = hoy.year"""





"""hoy = now.strftime('%d / %m / %Y')
print(hoy)"""