teste = []
teste.append('gustavo')
teste.append(30)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) 
print(teste)
print(galera)