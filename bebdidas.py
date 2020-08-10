# -*- coding: utf-8 -*-

class almacen:
    #ATRIBUTOS DE ALMACEN
    def __init__(self):
        self.listaDeProductos = []
    #METODOS DE ALMACEN
    def calcularPreciosBebidas(self):
        pass

    def calcularPrecioDeUnaMarca(self):
        pass

    def agregarProducto(self, producto):
        self.listaDeProductos.append(producto)

    def eliminarProducto(self, producto):
        self.listaDeProductos.remove(producto)

    def mostrarInformacion(self):
        pass

    def __repr__(self):
        return "Lista de productos: {}".format(self.listaDeProductos)



class bebidas:
    #ATRIBUTOS DE BEBIDAS
    def __init__(self, ide, litros, precio, marca):
        self.ide = ide
        self.litros = litros
        self.precio = precio
        self.marca = marca 
    #METODOS DEL ALMACEN
    #def __repr__(self):
    #    return "IDE: {}, litros: {}, precio: {}, marca: {}".format(self.ide, self.litros, self.precio, self.marca)


class aguaMineral(bebidas):
    #ATRIBUTOS DE BEBIDAS
    def __init__(self, ide, litros, precio, marca, origen):
        bebidas.__init__(self, ide, litros, precio, marca)
        self.origen = origen
    #METODOS DEL ALMACEN
    def __repr__(self):
        return "\nIDE: {}\n litros: {}\n precio: {}\n marca: {}\n origen: {}\n \n".format(self.ide, self.litros, self.precio, self.marca, self.origen)


class gaseosa(bebidas):
    def __init__(self, ide, litros, precio, marca, azucar, promocion):
        bebidas.__init__(self, ide, litros, precio, marca)
        self.azucar = azucar
        self.promocion = promocion
    def __repr__(self):
        return "\nIDE: {}\n litros: {}\n precio: {}\n marca: {}\n azucar: {}\n promocion: {}\n \n".format(self.ide, self.litros, self.precio, self.marca, self.azucar, self.promocion)


agua1 = aguaMineral(321, 2.5, 70, "agüita", "Manantial")


gaseosa1 = gaseosa(198, 2, 100, "cabalgata", 9,4)


almacen1 = almacen()
almacen1.agregarProducto(agua1)
almacen1.agregarProducto(gaseosa1)
print(almacen1)
print("-"*10,"apartir de abajo se elimina el ide 321","-"*10)
almacen1.eliminarProducto(agua1)
print(almacen1)
