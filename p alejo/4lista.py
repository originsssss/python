#4. Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor.

lista = []

for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    
mayor = max(lista)
cont = 0
for i in lista:
    if mayor == i:
        cont = cont + 1
print("El numero mayor se repite",cont," veces")
        