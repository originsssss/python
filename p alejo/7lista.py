#7. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el menor número primo.

lista = []

for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    
cont = 0
menor = min(lista)
for i in lista:
    for x in range(0,10):
        if menor % x == 0:
            cont = cont + 1

if cont == 0:
    print("El numero menor primo es", menor)
    
    