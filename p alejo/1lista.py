#1. Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.

lista = []
for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    
mayor = 0
for i in range(0,10):
    if lista[i] % 2 == 0:
        if lista[i] > mayor:
            mayor = lista[i]
            x = i
            
print("El numero mayor es ",mayor," y esta en la posicion ",x)