nome = str(input('qual o seu nome? '))
if nome == 'isabella':
    print('que nome bonito')
elif nome == 'paulo' or nome == 'maria' or nome == 'pedro':
    print('seu nome é popular no brasil')
elif nome in 'ana claudia juliana jessica':
    print('que belo nome feminino')
else:
    print('que nome feio')