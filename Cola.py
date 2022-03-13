from orden import Orden
from graphviz import Digraph
from os import system, startfile

class Cola():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
    
    def Vacia(self):
        return self.primero == None
    
    def agregarAlFinal(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Orden(dato)
        else:
            aux = self.ultimo
            self.ultimo = Orden(dato)
            aux.siguiente = self.ultimo
        self.size += 1
    
    #Devuelve el Nodo Orden
    def eliminarAlInicio(self):
        ordenTerminada : Orden = None
        self.size += 1
        if self.Vacia():
            return None
        elif self.primero == self.ultimo:
            ordenTerminada = self.primero
            self.primero = self.ultimo = None
            return ordenTerminada.dato #Se devuelve la unica Orden  
        else:
            ordenTerminada = self.primero
            #el apuntador de la cabecera oasa al siguiente nodo ya que FIFO
            self.primero = self.primero.siguiente
            return ordenTerminada.dato #Se devuelve la Orden
    #Graficar  
    def showIMG(self):
        actual = self.primero
        cont = 0
        dot  = Digraph("G", format="png", graph_attr={"rankdir":"LR", "bgcolor":"steelBlue"},
                        node_attr={"style":"filled", "shape":"rect"},
                        edge_attr={"color":"#999999", "fontcolor":"#888888"})
        while actual:
            dot.node(f"node{str(cont)}", str(actual.dato),{"color":"white", "fontcolor":"white", "fillcolor":"IndianRed"})
            if actual != self.primero:
                dot.edge(f"node{str(cont-1)}", f"node{str(cont)}")
            actual = actual.siguiente
            cont += 1
        nombre = "cola_actual"
        dot.save(filename=f"{nombre}.dot", directory="../practica 1/")
        system(f"dot -Tpng {nombre}.dot -o {nombre}.png")
        startfile(f"{nombre}.png")
        
    def mostrarOrdenes(self):
        print("\n Ordenes pendientes:")
        if self.Vacia():
            print("No hay Ordenes pendientes :)")
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente