print ("METODOS DE ENVIO")
print ("GET")
print ("POST")
print ("PUT")
print ("DELETE")
print ("SALIR")
opc = (input("Escriba lo que desea ")).upper()
print (opc)

match opc:
    case "GET":
        print("Fetching Resource...")
    case "POST":
        print("Creating Resource...")
    case "PUT":
        print("Updating Resource...")
    case "DELETE":
        print("Deleting Resource...")
    case "SALIR":
        print("Saliendo...")
    case _:
        print("Unsupported HTTP method.")

