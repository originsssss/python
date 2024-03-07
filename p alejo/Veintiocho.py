#28.Leer 2 números enteros y determinar cual de los dos tiene mayor cantidad de dígitos primos.

lista = [2,3,5,7]
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))

cont1 = 0
x = 0
while num1 > 0:
    dig1 = num1 % 10
    num1 = num1 // 10
    for i in range(2,dig1):
        div = dig1 % i
        if div == 0:
            cont1 = cont1 + 1      
    if dig1 in lista:
        x = x + 1


cont2 = 0
l = 0           
while num2 > 0:
    dig2 = num2 % 10
    num2 = num2 // 10
    for n in range(2,dig2):
        div2 = dig2 % n
        if div2 == 0:
            cont2 = cont2 + 1
    if dig2 in lista:
        l = l + 1
    
        
if x > l:
    print("El primer numero tiene mas digitos primos") 

if l > x:
    print("El segundo numero tiene mas digitos primos")
    
  