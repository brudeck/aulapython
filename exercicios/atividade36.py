nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
media = (nota1 + nota2) / 2
print("Média: {:.1f}".format(media))
if media < 5.0:
    print("Resultado: Reprovado")
elif 5.0 <= media < 7.0:
    print("Resultado: Recuperação")
else:
    print("Resultado: Aprovado")