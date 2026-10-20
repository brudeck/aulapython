from datetime import datetime
dados = {}
dados ['nome'] = str(input('digite seu nome'))
nasc = int(input('em qual ano você nasceu?0'))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('qual é o seu ctps'))
if dados ['ctps'] !=0:
    dados ['contratação'] = int(input('ano de contratação'))
    dados ['salário'] = float(input('salário'))
    dados ['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')