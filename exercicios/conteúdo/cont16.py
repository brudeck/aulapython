# Brasil = []
# estado1 = {'uf': 'rio de janeiro', 'sigla':'rj'}
# estado2 = {'uf': 'são paulo', 'sigla':'sp'}
# Brasil.append(estado1)
# Brasil.append(estado2)
# print(estado1)
# print(estado2)
# print(Brasil [0])
# print(Brasil [1])
# print(Brasil[0]['uf'])
# print(Brasil[1]['sigla'])

estado = {}
brasil = []
for c in range(0,3):
    estado ['uf'] = str(input('unidade federativa'))
    estado ['sigla'] = str(input('sigla do estado'))
    brasil.append(estado.copy ())
for e in brasil:
    for k,v in e .items():
        print(f'o campo {k} tem o valor {v}')