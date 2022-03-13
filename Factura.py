from graphviz import Digraph
from os import system, startfile

class Orden():

    def __init__(self, nombre, nit, telefono):
        #Los datos de mi cliente directamente
        self.cliente = nombre
        self.nit=nit
        self.tel=telefono
        #una lista de pizzas
        self.pizzas = lista_pizzas()
    
    def getCliente(self):
        return self.cliente
    
    def getPizzas(self):
        return self.pizzas
    
    
