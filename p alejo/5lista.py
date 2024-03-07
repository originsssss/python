#5. Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números tienen, de los almacenados allí, tienen menos de 3 dígitos.

lista = []

for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    lista.append(num)
    
cont = 0    
for i in lista:
    if i < 99:
        cont = cont + 1
    
print("hay",cont," que tienen menos de tres digitos")