#2.	Una persona no tiene claridad sobre
# el dispositivo que va a comprar para su computadora. 
# La decisión la tomará de acuerdo con una bonificación que 
# recibirá de parte de la empresa donde labora. 
# Si recibe menos de $ 50.000 de bonificación comprará una cámara web, 
# sirecibe entre $50000 y $200 000 comprará un subwoofer; 
# si recibe más de $200.000 y hasta $ 500 000 se comprará un disco externo, 
# si recibe más de $500.000 y hasta $1.000.000 se comprará una multifuncional 
# y si recibe más de $ 1.000.000 se comprará un proyector.

# Bonificacion
bonificacion = 100000

#Determinar que compra
if bonificacion < 50000:
    dispositivo = "Camara Web"
elif 50000 <= bonificacion <= 200000:
    dispositivo = "Subwoofer"
elif 200000 < bonificacion <= 500000:
    dispositivo = "Disco externo"
elif 500000 < bonificacion <= 1000000:
    dispositivo = "Multifuncional"
else:
    dispositivo = "Proyector"

#Muestra el resultado
print("Con una bonificacion de", bonificacion , "comprara un" , dispositivo)
