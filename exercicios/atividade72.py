pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (kg): ')))
    
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
            
    pessoas.append(dados[:])
    dados.clear()
    
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'B) O maior peso foi de {maior_peso}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()

print(f'C) O menor peso foi de {menor_peso}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()
