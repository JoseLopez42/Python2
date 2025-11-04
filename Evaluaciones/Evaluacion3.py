class Persona:
    def __init__(self, nombre, edad, genero, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.altura = altura
        self.imc = self.calcular_imc()

    # Método para calcular el IMC
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    # Método para interpretar el IMC según el género
    def interpretar_imc(self):
        if self.genero.lower() == "masculino":
            if self.imc < 20:
                return "Bajo peso"
            elif 20 <= self.imc <= 24.9:
                return "Normal"
            elif 25 <= self.imc <= 29.9:
                return "Obesidad leve"
            elif 30 <= self.imc <= 40:
                return "Obesidad severa"
            elif self.imc > 40:
                return "Obesidad muy severa"
        elif self.genero.lower() == "femenino":
            if self.imc < 20:
                return "Bajo peso"
            elif 20 <= self.imc <= 23.9:
                return "Normal"
            elif 24 <= self.imc <= 28.9:
                return "Obesidad leve"
            elif 29 <= self.imc <= 37:
                return "Obesidad severa"
            elif self.imc > 37:
                return "Obesidad muy severa"
        else:
            return "Género no reconocido"

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, IMC: {self.imc:.2f}, Estado: {self.interpretar_imc()}"

def agregar_persona():
    try:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        genero = input("Ingrese el género (Masculino/Femenino): ").capitalize()
        peso = float(input("Ingrese el peso (kg): "))
        altura = float(input("Ingrese la altura (m): "))

        persona = Persona(nombre, edad, genero, peso, altura)
        return persona
    except ValueError:
        print("Error en los datos ingresados. Asegúrese de ingresar números correctamente.")
        return None

def mostrar_reporte(personas):
    for persona in personas:
        print(persona.mostrar_info())
        print("-" * 50)

def main():
    personas = []

    while True:
        print("\n--- Menu ---")
        print("1. Agregar persona")
        print("2. Ver reporte de IMC")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            persona = agregar_persona()
            if persona:
                personas.append(persona)
        elif opcion == "2":
            if personas:
                mostrar_reporte(personas)
            else:
                print("No hay personas para mostrar.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
