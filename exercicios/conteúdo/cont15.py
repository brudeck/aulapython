# teste = []
# teste.append('gustavo')
# teste.append(30)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:]) 
# print(teste)
# print(galera)

# galera = [['joão',19],['ana',33],['joaquim',17],['maria',45]]
# print(galera[2] [1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

 galera = []
 dado = []
 tomai = tomen = 0
 for c in range (0,3):
     dado.append(str(input('nome')))
     dado.append(int(input('idade')))
     galera.append(dado[:])
     dado.clear()
 print(galera)

for p in galera:
    if p[1] >=18:
        print(f'(p[0]} é maior de idade')
        tomai += 1
    else:
        print(f'(p[0]) é menor de idade')
        tomen += 1
print(f'Temos (tomai) maiores de idade e {tomen) menores de idade)