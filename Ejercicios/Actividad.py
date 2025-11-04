print("Bienvenido a la tienda 🥤")

print("1 - Gaseosa grande ($5000)")
print("2 - Gaseosa pequeña ($3000)")
print("S - Salir")

total = 0

while True:
    opcion = input("Elige una opción: ").upper()

    if opcion == "S":
        break
    elif opcion == "1":
        total += 5000
        print("Agregaste una gaseosa grande.")
        print("1 - Gaseosa grande ($5000)")
        print("2 - Gaseosa pequeña ($3000)")
        print("S - Salir")
    elif opcion == "2":
        total += 3000
        print("Agregaste una gaseosa pequeña.")
        print("1 - Gaseosa grande ($5000)")
        print("2 - Gaseosa pequeña ($3000)")
        print("S - Salir")
    else:
        print("Opción no válida.")

print("Total a pagar: $", total)
print("¡Gracias por tu compra!")