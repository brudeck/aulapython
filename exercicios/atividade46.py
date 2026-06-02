primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = primeiro + 10 * razao
for c in range(primeiro, decimo, razao):
    print(f'{c}', end= '->')
print('acabou')