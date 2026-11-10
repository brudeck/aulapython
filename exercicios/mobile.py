print("=== PESQUISA: HÁBITOS DE CONSUMO ===")

alunos = int(input("Quantos alunos serão entrevistados? "))

produtos = []
bebidas = []
gastos = []

for i in range(alunos):
    print("\nAluno", i + 1)

    produto = input("Produto mais comprado: ")
    bebida = input("Bebida mais consumida: ")
    gasto = float(input("Quanto gasta por dia (R$): "))

    produtos.append(produto.lower())
    bebidas.append(bebida.lower())
    gastos.append(gasto)

print("\n=== RESULTADO DA PESQUISA ===")

produto_favorito = max(set(produtos), key=produtos.count)
bebida_favorita = max(set(bebidas), key=bebidas.count)

media = sum(gastos) / alunos

print("Produto mais comprado:", produto_favorito)
print("Bebida mais consumida:", bebida_favorita)
print("Gasto médio diário: R$", round(media, 2))
print("Total de alunos entrevistados:", alunos)
