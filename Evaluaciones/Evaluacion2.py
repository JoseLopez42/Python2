# 4.	Un gimnasio desea determinar al Índice de Masa Corporal 
# IMC para sus afiliados. Hasta que el entrenador determine cuando 
# terminar se debe hacer el cálculo, sabiendo que la fórmula es 
# IMC = Peso / altura².
# Al finalizar se debe mostrar el nombre de la persona, la edad, genero 
# e indicar el estado del IMC de acuerdo con la siguiente tabla.

#Datos del Afiliado
nombre = "Jose Lopez"
edad = 20
genero = "Masculino" #"Masculino" o "Femenino"
peso = 70
altura = 1.78

#Calculo del IMC
imc = peso // (altura ** 2)

#Imprimir
print ("Nombre:", nombre)
print ("Edad:", edad)
print ("Genero:", genero)
print ("IMC:", imc)

#Segun genero
if genero == "Masculino" and imc<20:
        print("Su estado del IMC es : Bajo Peso")
if genero == "Masculino" and imc >= 20 and imc <= 24.9:
        print("Estado del IMC: Normal")
if genero == "Masculino" and imc >= 25 and imc <= 29.9:
        print("Estado del IMC: Obesidad leve")
if genero == "Masculino" and imc >= 30 and imc <= 40:
        print("Estado del IMC: Obesidad severa")
if genero == "Masculino" and  imc > 40:
        print("Estado del IMC: Obesidad muy severa")
if genero == "Femenino" and imc < 20:
        print("Estado del IMC: Bajo peso")
if genero == "Femenino" and imc >= 20 and imc <= 23.9:
        print("Estado del IMC: Normal")
if genero == "Femenino" and imc >= 24 and imc <= 28.9:
        print("Estado del IMC: Obesidad leve")
if genero == "Femenino" and imc >= 29 and imc <= 37:
        print("Estado del IMC: Obesidad severa")
else:
        print("Estado del IMC: Obesidad muy severa")