#3. Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números terminados en 4.

lista = []
for i in range(0,10):
    num = int(input("Ingese un numero: "))
    lista.append(num)
    
    
for i in range(0,10):
    if lista[i] % 10 == 4: 
     print("Los numeros terminados en cuatro estan en la posicion", i )