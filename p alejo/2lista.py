#2. Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y mostrarlo en pantalla.

lista = []
n = 0
nu = 1

for i in range(0,10):
    lista.append(n)
    m = n + nu
    n = nu
    nu = m
print(lista)