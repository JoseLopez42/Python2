#1
pal =str(input("Ingrese una palabra "))
for x in range (1, 11):
    print (x, pal) 
print ()

#2
edad =int(input("Ingrese su edad "))
if edad>0:
    for x in range (1, edad + 1):
        print ("Ha tenido", x, "Años")
    if edad >=18:
        print ("Es Mayor de Edad")
    else:
        print ("Es Menor de Edad")
else:
    print ("Edad Invalida")
print ()

#3
num =int(input("Ingrese un numero entero positivo "))
if num <0:
    print("Numero Invalido")
for x in range (1, num+1, +2):
    print(x, end=", ")
print ()
print ()

#4
nume =int(input("Ingrese numero a multiplicar: "))
for x in range (1, 11):
    print("Numero", nume, "x", x, "=", (nume*x))

print()
print("FIN")