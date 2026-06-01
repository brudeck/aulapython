preco_original = float(input('digite o preço do produto'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] a vista (dinheiro/cheque)
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('qual é a opção?'))
if opcao == 1:
    total = preco_original - (preco_original * 15 / 100)
elif opcao == 2:
    total = preco_original - (preco_original * 8 / 100)
elif opcao == 3:
    total = preco_original
    parcela = total / 2
    print(f'sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS.')
elif opcao == 4:
    total = preco_original + (preco_original * 25 / 100)
    tot_parc = int(input('quantas parcelas? '))
    parcela = total / tot_parc
    print(f'sua compra será parcelada em {tot_parc}x de R$ {parcela:.2f} com juros.')
else:
    total = preco_original
    print('opcçao invalida de pagamento, tente novamente!')

print(f'sua compra de R$ {preco_original:.2f} vai custar R$ {total:.2f} no final.')