from ListaLigada.NodoS import NodoS
from graphviz import Digraph

class ListaS:
    def __init__(self):
        self.primero=None
        self.size = 0

    def insertar(self, dato):
        nuevo = NodoS(dato) # Creamos el nuevo nodo
        if self.primero == None: # Si no hay nada en la lista
            self.primero = nuevo
        else: # Si ya hay algo 
            actual = self.primero # Obtener el primero de la lista
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.size += 1

    def imprimir(self):
        actual = self.primero
        if actual is None:
            print('la lista está vacía')
            return
        while actual.siguiente != None:
            print(actual.dato)
            actual = actual.siguiente
        print(actual.dato)

    def eliminar(self, dato):
        actual = self.primero
        anterior = None
        while actual is not None:
            if actual.dato == dato:
                if anterior is None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.size -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def graficar(self, nom="Lista"):
        if self.primero is None:
            return False
        
        try:
            dot = Digraph("Lista", format="png")
            dot.attr(rankdir="LR", size="8,5")

            dot.node_attr.update(shape="circle", style="filled", color="#F2B366")

            actual = self.primero
            while actual is not None:
                #crear nodo
                dot.node(str(id(actual)), label=str(actual.dato))
                actual = actual.siguiente

            actual = self.primero
            while actual is not None:    
                #enlaces
                if actual.siguiente:
                    dot.edge(str(id(actual)), str(id(actual.siguiente)), constraint='true')
                actual = actual.siguiente
            
            dot.render(nom, view=True)
            return True
        
        except Exception as e:
            return False