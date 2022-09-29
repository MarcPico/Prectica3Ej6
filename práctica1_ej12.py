#Introducir variable
horas=float(input('Número de horas de estacionamiento: '))
dias=horas/24

#Control max/min horas
if horas<24 or horas>720:
    print('Número de horas no válido.')
else:
    if dias==1:
        print('El importe a pagar son 11€.')
    elif dias>1 and dias<6:
        precio=11+6*dias
        print('El importe a pagar son {0}€.'.format(precio))
        print('Gracias por elegir nuestro estacionamiento.')
