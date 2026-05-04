viagem = float(input('qual a distância da sua viagem?'))
curta = 0.5 * viagem
longa = 0.45 * viagem
print('você está prestes a começar uma viagem de {}km'.format(viagem))
if viagem <=200:
    print('e o preço da sua viagem será de R${}'.format(curta))
else:
    print('e o preço da sua viagem será de R${}'.format(longa))