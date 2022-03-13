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
    
    #Grafica el pedido 
    def showOrden(self):
        cont = 0
        dot  = Digraph("G", format="png", graph_attr={"rankdir":"LR", "bgcolor":"steelBlue"},
                        node_attr={"style":"filled", "shape":"rect"},
                        edge_attr={"color":"#999999", "fontcolor":"#888888"})
        
        dot.node(f"node{str(cont)}", self.__str__() ,{"color":"white", "fontcolor":"white", "fillcolor":"#2ECC71"})
            
        nombre = "Orden Lista"
        dot.save(filename=f"{nombre}.dot", directory="../IPC2_Practica1_202002536/")
        system(f"dot -Tpng {nombre}.dot -o {nombre}.png")
        startfile(f"{nombre}.png")
