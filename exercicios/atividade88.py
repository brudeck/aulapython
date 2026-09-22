matriz = []
print("Digite os valores para preencher a matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print("\nMatriz Resultante:")
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()  