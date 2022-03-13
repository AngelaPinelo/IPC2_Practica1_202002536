#Nodo Orden 
class Orden():
#No voy a utilizar apuntador anterior por ser una cola gg
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None
    
    def getDato(self):
        return self.datos