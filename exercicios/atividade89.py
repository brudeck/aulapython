matriz = [[0,0,0], [0,0,0], [0,0,0]]
total3 = maior = somapar = 0
for 1 in range (0,3):
    for c in range (0,3):
        matriz [1][c] = int(input(f'digite um valor para [(1), (c)]:'))
        if matriz [1] [c] % 2 == 0:
            somapar += matriz [1][c]
        if c == 2:
            total3 + matriz [1][c]
        if 1 == 1 and c== 0:
            maior = matriz [1][c]
        elif 1 == 1 and c !=0 and matriz [1] [c]> maior:
            maior = matriz [1][c]
    for 1 in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[1][c]}]', end='')
            print()
            print (f'A soma dos valores pares é (somapar)')
            print(f'A soma dos números da terceira coluna é igual a {total3}')
            print(f'O maior valor da da linha 2 é {maior}')