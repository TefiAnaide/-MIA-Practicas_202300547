from graphviz import Digraph

class ListaIndexada:
    def __init__(self):
        self.datos = []
        self.inidices = []

    def insertar(self, dato):
        self.datos.append(dato)
        self.inidices.append(len(self.datos)-1)

    def eliminar(self, dato):
        if dato in self.datos:
            posicion = self.datos.index(dato)
            self.datos.pop(posicion)
            self.inidices.pop(posicion)

            self.inidices = list(range(len(self.datos)))
            return True
        else:
            print('posicion invalida')
            return False
        
    def imprimir(self):
        for i, d in zip(self.inidices, self.datos):
           print(f'{i} | {d}')

    def graficar(self):
        dot = Digraph()
        dot.attr(rankdir='TB')

        table = "<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0'>"
        table += "<TR><TD><B>Índice</B></TD><TD><B>Dato</B></TD></TR>"
        for i, d in zip(self.inidices, self.datos):
            table += f"<TR><TD>{i}</TD><TD>{d}</TD></TR>"
        table +="</TABLE>>"

        dot.node("tabla", table, shape="plaintext")        
        dot.render('Lista', format='png', cleanup=False)
        dot.view()