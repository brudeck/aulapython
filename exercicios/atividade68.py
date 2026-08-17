# Criação da tupla única com produtos e preços na sequência
listagem = (
    "Lápis", 1.75,
    "Borracha", 2.00,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Canetas", 22.30,
    "Livro", 34.90
)

# Cabeçalho da tabela
print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)

# Estrutura de repetição para tabular os dados
for posicao in range(0, len(listagem)):
    # Se a posição for par, trata-se do nome do produto
    if posicao % 2 == 0:
        print(f"{listagem[posicao]:.<30}", end="")
    # Se a posição for ímpar, trata-se do preço
    else:
        print(f"R$ {listagem[posicao]:>7.2f}")

print("-" * 40)
