
print('Jaume LLoret volvió a estar aquí')

print('Hello world!')
print('Jaume LLoret estuvo aquí')

#Intoducir variables
kg=float(input('Intoduce tu peso (en kg): '))
h=float(input('Introduce tu altura (en m): '))

#Operaciones con variables
IMC= round(kg/h**2, 2)

#Determinación de resultado
print('Su IMC es de {0} kg/m^2.'.format(IMC))
if IMC<=24.99 and IMC>=18.5:
    print('Su peso es normal.')
elif IMC<18.5:
    print('Está bajo de peso.')
elif IMC>=25 and IMC<30:
    print('Tiene sobrepeso.')
elif IMC>=30 and IMC<40:
    print('Padece obesidad.')
else:
    print('Sufre de obesidad mórbida.')
