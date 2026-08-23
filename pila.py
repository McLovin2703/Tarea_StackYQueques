class PilaVaciaError(Exception):
    def __init__(self, mensaje="la pila está vacía"):
        super().__init__(mensaje)

class PilaArreglo:
    def __init__(self):
        self.elementos = [None] * 10
        self.tope = -1
    
    def apilar(self, elemento):
        if self.tope + 1 == len(self.elementos):
            nuevo = [None] * (len(self.elementos) * 2)
            for i in range(self.tope + 1):
                nuevo[i] = self.elementos[i]
            self.elementos = nuevo
        self.tope += 1
        self.elementos[self.tope] = elemento
    
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar")
        elemento = self.elementos[self.tope]
        self.elementos[self.tope] = None
        self.tope -= 1
        return elemento
    
    def cima(self):
        if self.esta_vacia():
            raise PilaVaciaError("la pila está vacía.")
        return self.elementos[self.tope]
    
    def esta_vacia(self):
        return self.tope == -1
    
    def tamano(self):
        return self.tope + 1
    
    def vaciar(self):
        for i in range(self.tope + 1):
            self.elementos[i] = None
        self.tope = -1

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class PilaListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tam = 0
    
    def apilar(self, elemento):
        self.cabeza = Nodo(elemento, self.cabeza)
        self.tam += 1
    
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.tam -= 1
        return dato
    
    def cima(self):
        if self.esta_vacia():
            raise PilaVaciaError("la pila está vacía.")
        return self.cabeza.dato
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def tamano(self):
        return self.tam
    
    def vaciar(self):
        self.cabeza = None
        self.tam = 0

def probar_pila(pila):
    resultados = []
    resultados.append(str(pila.esta_vacia()))
    for i in range(1, 13):
        pila.apilar(i)
    resultados.append(str(pila.tamano()))
    resultados.append(str(pila.cima()))
    resultados.append(str(pila.desapilar()))
    resultados.append(str(pila.cima()))
    resultados.append(str(pila.tamano()))
    resultados.append(str(pila.esta_vacia()))
    pila.vaciar()
    resultados.append(str(pila.esta_vacia()))
    try:
        pila.cima()
        resultados.append("sin excepción")
    except PilaVaciaError as e:
        resultados.append(str(e))
    try:
        pila.desapilar()
        resultados.append("sin excepción")
    except PilaVaciaError as e:
        resultados.append(str(e))
    return resultados

p1 = PilaArreglo()
p2 = PilaListaEnlazada()

r1 = probar_pila(p1)
r2 = probar_pila(p2)

print("Resultados Pila Arreglo:")
for i, r in enumerate(r1, 1):
    print(f"{i}: {r}")

print("\nResultados Pila Lista Enlazada:")
for i, r in enumerate(r2, 1):
    print(f"{i}: {r}")

print(f"\ntienen el mismo resultado? {r1 == r2}")