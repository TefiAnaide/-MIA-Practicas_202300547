from ListaDobleLigada.NodoD import NodoD
from graphviz import Digraph

class ListaD:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self, dato):
        nuevo = NodoD(dato)
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
        
        self.size += 1

    def eliminar(self, dato):
        actual = self.primero
        while actual != None:
            #para buscar el dato
            if actual.dato == dato:
                #si es el primer nodo
                if actual == self.primero:
                    self.primero = actual.siguiente
                    if self.primero is not None:
                        self.primero.aterior = None #para vaciar el nodo anterior
                #en caso sea el último nodo
                elif actual == self.ultimo:
                    self.ultimo = actual.anterior
                    if self.ultimo is not None: #para vaciar el nodo siguiente
                        self.ultimo.siguiente = None
                #si está en medio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                self.size -= 1
                return True
            
            actual = actual.siguiente
        return False
                    
    def imprimir(self):
        actual = self.primero
        while actual != None:
            print(actual.dato)
            actual = actual.siguiente

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
                    dot.edge(str(id(actual.siguiente)), str(id(actual)), constraint='true')
                actual = actual.siguiente
            
            dot.render(nom, view=True)
            return True
        
        except Exception as e:
            return False

    