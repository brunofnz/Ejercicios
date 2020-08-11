#Un supermercado maneja el catálogo de los productos que vende. De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no. Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

#Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad. Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:

#precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9

#El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de productos que comercializa y la suma total de los precios de los mismos.


#Espacio de clases

class supermercado:
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion

    def cantidadTotalProductos():
        pass

class producto:
    def __init__(self, marca, tipo, precio, precioCuidado = False, primeraNecesidad = False):
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.precioCuidado = precioCuidado
        self.primeraNecesidad = primeraNecesidad

    def __repr__(self):
        return "Marca: {}\n Tipo: {}\n Precio: {}\n PrecioCuidado: {}\n Primera necesidad: {}\n".format(self.marca, self.tipo,self.precio, self.precioCuidado, self.primeraNecesidad)

class catalogo:
    def __init__(self):
        self.producto = None
        self.productos = list()
    
    def __repr__(self):
        return "{}".format(self.productos)
    
    def agregarProducto(self, marca, tipo, precio, precioCuidado = False, primeraNecesidad = False):
        self.producto = producto(marca, tipo, precio, precioCuidado, primeraNecesidad)
        self.productos.append(self.producto)
        self.producto = None


#CODIGO PRINCIPAL

supermercado1 = supermercado('Carrefour','Av. San Martin 446')
catalogo1 = catalogo()
catalogo1.agregarProducto('Serenisima', 'Leche',70,True,True)
print(catalogo1)




"""producto1 = producto('Coca Cola', 'Gaseosa', 120)
print(producto1)
producto2= producto('Serenisima', 'Leche',70,True,True)
print(producto2)"""




