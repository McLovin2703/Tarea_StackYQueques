n = [1, 2, 4, 7, 11, 66 ]
m = [3, 2, 1]
def ultimo():
    if n:
        print("el ulrimo numero de la lista es:")
        return n[-1]
    else:
        return "Horror, La lista esta vacia"
        
def buscar():
    b = int(input("INgrese el numero que quiere buscar: "))
    for i in n:
        if b == i:
            return f"El numero {b} esta en la lista en la posicion {n.index(b)}"
    return -1

def du():
    vistos = set()
    duplicados = set()

    for i in n:
        if i in vistos:
            duplicados.add(i)
        else:
            vistos.add(i)

    return print("Los numero duplicados son:", list(duplicados))

def dividir():
    divisiones = 0
    a = float(input("ingrese un numero: "))


    while a>1:
        a = a/2
        divisiones += 1
        

    print("El numero de divisiones fue:", divisiones)
    return print("lo que quedo:", a)

def busqueda_binaria(n):
    n.sort()
    b = int(input("Que numero desea buscar?"))

    on = 0
    sup = len(n)-1
        
    
    while on <= sup:
        medio = (on+sup)//2

        if n[medio] == b:
            return f"Encontrado {b} esta en la lista en la posicion {n.index(b)+1}"
            

        elif n[medio] < b:
            on = medio + 1
        else:
            sup = medio-1

    return -1

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



def iteracion(n):
    for i in range(n):
        j = 1

        while j < n:
            j = j * 2

    
def procesar(n, m):

    suma = 0

    for elemento in n:
        suma += elemento

    producto = 1

    for elemento in m:
        producto *= elemento

    return suma, producto



while True:

    print("---------------------------------------")
    print(" *espacio* ")
    print("lista 1: ", n)
    print("lista 2: ", m)

    print("1. Ultimo numero de la lista")
    print("2. Buscar")
    print("3. buscar Duplicados")
    print("4. Dividir en dos un numero varias veces")
    print("5. Busqueda binaria")
    print("6. Fibonacci")
    print("7. Iteracion")
    print("8. Procesar las listas")
    print("0. Salir")

    op = int(input("Opcion: "))

    if op == 1:
        print(ultimo())
    elif op == 2:
        print(buscar())
    elif op == 3:
        du()
    elif op == 4:
        dividir()
    elif op == 5:
        print(busqueda_binaria(n))
    elif op == 6:
        numero = int(input("Numero: "))
        print(fibonacci(numero))
    elif op == 7:
        numero = int(input("Numero: "))
        iteracion(numero)
        print("Iteracion terminada")
    elif op == 8:
        print(procesar(n, m))
    elif op == 0:
        break



