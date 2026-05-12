from datetime import date 
ano = int(input("ano de nascimento"))
idade = date.today().year - ano
tempopassado = idade - 18
tempofaltante = 18 - idade 
print("quem nasceu em {} tem {} anos".format(ano, idade))
if idade > 18:
    print("voce ja devia ter se alistado há {} anos".format(tempopassado))
elif idade < 18:
    print("voce ainda não tem idade para se alistar, faltam {} anos".format(tempofaltante))
else:
    print("voce deve se alsitar esse ano")