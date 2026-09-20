class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class busqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar(self.raiz, nuevo_nodo)

    def _insertar(self, nodo, nuevo_nodo):
        if nuevo_nodo.valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = nuevo_nodo
            else:
                self._insertar(nodo.izquierda, nuevo_nodo)

        elif nuevo_nodo.valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = nuevo_nodo
            else:
                self._insertar(nodo.derecha, nuevo_nodo)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False

        if nodo.valor == valor:
            return True

        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def mostrar_inorden(self, nodo):
        if nodo is not None:
            self.mostrar_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.mostrar_inorden(nodo.derecha)



arbol = busqueda()

arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Árbol en orden:")
arbol.mostrar_inorden(arbol.raiz)
print("" \
"")

x = int(input("que numero quiere buscar?: "))
print("¿Esta el ", x, "?")
print(arbol.buscar(x))