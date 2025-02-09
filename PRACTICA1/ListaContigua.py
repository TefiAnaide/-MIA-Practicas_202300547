from graphviz import Digraph

class ListaContigua:
    def __init__(self):
        self.lista = []

    def insertar(self, dato):
        self.lista.append(dato)

    def eliminar(self, dato):
        self.lista.remove(dato)

    def imprimir(self):
        print(self.lista)

    def graficar(self):
        dot = Digraph()
        dot.attr(rankdir='LR')

        with dot.subgraph() as sub:
            sub.attr(rank='same')
            sub.node("head","Lista Contigua", shape="plaintext")
            table="<<TABLE BORDER='1' CELLBORDER='1' CELLSPACING='0'>"
            table += "<TR>"
            for dato in self.lista:
                table += f"<TD>{dato}</TD>"
            table += "</TR></TABLE>>"
            sub.node("tabla", table, shape="plaintext")
            sub.edge("head", "tabla")
        
        dot.render('Lista', format='png', cleanup=False)
        dot.view()