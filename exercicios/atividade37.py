peso = float(input('qual é o seu peso? (kg)'))
altura = float(input('qual é a sua altura? (m)'))
imc = peso/(altura**2)
print('o imc dessa pessoa é de {.:1f}'.format(imc))
if imc < 18.5:
    print('voce esta abaixo do peso normal')
elif 18.5 <= imc <25:
    print('parabens! voce esta com o peso ideal')
elif 25 <= imc < 30:
    print('voce esta com sobrepeso')
elif 30 <= imc < 40:
    print('voce esta com obesidade, cuidado')
else:
    print('voce esta com obesidade morbida, cuidado')