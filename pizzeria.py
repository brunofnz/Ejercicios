class pizza:
    def __init__(self, nombre, tamaño, variedad, tipo,ingredientes, precio):
        self.nombre = nombre
        self.tamaño = tamaño
        self.variedad = variedad
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.precio = precio
        #Variables locales de la clase

    def __repr__(self):
        return "Nombre:\t\t{}\nTamaño:\t\t{}\nVariedad:\t{}\nTipo:\t\t{}\nPrecio:\t\t${}".format(self.nombre,self.tamaño,self.variedad,self.tipo,self.precio)
   
    def getTamaño(self, tamaño):
        return self.tamaño
    
    def setTamaño(self, tamaño):
        self.tamaño = int(tamaño)
        

#Espacio de funciones

conjunto = [8,10,12]
def segunPorcion(tamaño,pizza):
    if (tamaño in conjunto):
        pizza.setTamaño(tamaño)
    else:
        print("El tamaño seleccionado no es correcto")

pizza1 = pizza("Pizza",8,0,0,0,0)
print(pizza1)
print("")
segunPorcion(6,pizza1)
print(pizza1)




"""class Mostrador:
    def __init__ (self,fecha=0,hora=0,cantidadDePizza,demoraEstimada):
        self.cantidadDePizza = cantidadDePizza
        self.fecha = fecha
        self.hora = hora
        self.demoraEstimada = demoraEstimada
    def __repr__(self):
        return "Cantidad: {},\nFecha de pedidio: {}\nHora de pedido: {}\nDemora estimada: {}".format(self.cantidadDePizza,self.fecha,self.hora,self.demoraEstimada)
   
    def mostrarMenu (self):
        pass

class pedido:
    def __init__ (self,nombreCliente):
        self.nombreCliente = nombreCliente
    def __repr__(self):
        return "Cliente: {}".format(self.nombreCliente)


    def masPedidos (self):
        Tipo = list()
        self.tipo.append(Tipo)
        # moda                                                                                   
        repeticiones = 0                                                                         
        for i in Tipo:                                                                              
            self.tipo = Tipo.count(i)                                                             
            if self.tipo > repeticiones:                                                       
                repeticiones = self.tipo                                                       
                                                                                                                                                                    
        for i in Tipo:                                                                              
            apariciones = Tipo.count(i)                                                             
            if apariciones == repeticiones and i not in Tipo:                                   
                Tipo.append(i)                                                                  
                                                                                                
        print ("El tipo de pizza más pedido es:", Tipo) 

        
    def variedadMasPedida(self):
        Variedad = list()
        self.variedad.append(Variedad)
        # moda                                                                                   
        repeticiones = 0                                                                         
        for i in Variedad:                                                                              
            self.variedad = Variedad.count(i)                                                             
            if self.variedad > repeticiones:                                                       
                repeticiones = self.variedad                                                       
                                                                                                                                                                    
        for i in Variedad:                                                                              
            apariciones = Variedad.count(i)                                                             
            if apariciones == repeticiones and i not in Variedad:                                   
                Variedad.append(i)                                                                  
                                                                                                
        print ("La variedad de pizza más pedida es:", Variedad) """
