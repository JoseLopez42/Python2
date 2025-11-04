print ("METODOS DE ENVIO")
print ("1. GET")
print ("2. POST")
print ("3. PUT")
print ("4. DELETE")
print ("5. SALIR")
opc = int(input("Escoja la opcion que desea : "))
print (opc)

while (opc != 5):
    match opc:
        case 1:
            print("Entro al metodo GET")
        case 2:
            print("Entro al metodo POST")
        case 3:
            print("Entro al metodo PUT")
        case 4:
            print("Entro al metodo DELETE")
        case _:
            print("Si No")
    print ("METODOS DE ENVIO")
    print ("1. GET")
    print ("2. POST")
    print ("3. PUT")
    print ("4. DELETE")
    print ("5. SALIR")
    opc = int(input("Escoja la opcion que desea : "))
print ("Usted se salio del CICLO")