#6. Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el promedio entero de los datos del vector.

lista = []

for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    
suma = 0
for i in lista:
    suma = suma + i
    
pro = suma // 10
print("El promedio de los datos es: ",pro)