print("🧮 Bienvenido a la calculadora básica")

while True:
    print("\nSelecciona una operación:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("S - Salir")

    opcion = input("Elige una opción: ").upper()

    if opcion == "S":
        print("¡Hasta luego!")
        break
    elif opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                resultado = num1 + num2
                print("Resultado de la suma:", resultado)
            elif opcion == "2":
                resultado = num1 - num2
                print("Resultado de la resta:", resultado)
            elif opcion == "3":
                resultado = num1 * num2
                print("Resultado de la multiplicación:", resultado)
            elif opcion == "4":
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado de la división:", resultado)
                else:
                    print("Error: No se puede dividir entre cero.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa números válidos.")
    else:
        print("Opción no válida.")

    continuar = input("¿Deseas realizar otra operación? (S/N): ").upper()
    if continuar != "S":
        print("¡Gracias por usar la calculadora!")
        break
