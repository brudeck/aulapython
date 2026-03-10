nome = input ('qual é seu nome?')# 
print('prazer em conhece-lo{:20}!'.format(nome))
print('prazer em conhece-lo{:>20}!'.format(nome)) #espaçamento para a direita
print('prazer em conhece-lo{:<20}!'.format(nome)) #espaçamento para a esquerda
print('prazer em conhece-lo{:^20}!'.format(nome)) #alinhamento para o centro

num1 = int (input('digite um valor'))
num2 = int (input('digite outro valor'))
soma = num1+num2 #criar a variável para utilizar em outra parte do código
print ('a soma é {}'.format(soma))
