can =int(input("Ingrese cantidad de personas a solicitar datos "))
if (can <=0):
    print("Error, No se puede ingresar un Numero Negativo")

else:
    sumedad = 0
    sumalt = 0

#Datos
    for i in range(1, can+1, +1):
        print("Solitando Datos persona #",i)
        nombre = str(input("Ingrese el Nombre "))
        edad = int(input("Ingrese la Edad "))
        altura = float(input("Ingrese la Altura "))
        print ()

        sumedad = sumedad + edad
        sumalt = sumalt + altura

#Promedios
    promedad = sumedad / can
    promalt = sumalt / can

#Condiciones
    if (promedad<15) and (promalt<1.55):
        print ("El Promedio de edad fue" , promedad, ", El Promedio de Altura fue",promalt, ". Y su altura es un poco bajo para la edad")
    elif (promedad>15) and (promalt>1.68):
        print ("El Promedio de edad fue" , promedad, ", El Promedio de Altura fue",promalt, ", Y tu vas a ser Alto")
    else:
        print ("El Promedio de edad fue" , promedad, ", El Promedio de Altura fue",promalt, ", Y tu Promedio de altura es bueno")