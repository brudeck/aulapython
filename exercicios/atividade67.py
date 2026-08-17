numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

print("-" * 30)
print(f"Você digitou os valores: {numeros}")
print("-" * 30)
print(f"A) O valor 9 apareceu {numeros.count(9)} vez(es).")
if 3 in numeros:
    posicao = numeros.index(3) + 1
    print(f"B) O primeiro valor 3 foi digitado na {posicao}ª posição.")
else:
    print("B) O valor 3 não foi digitado em nenhuma posição.")
print("C) Os números pares digitados foram: ", end="")
tem_par = False
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")
        tem_par = True
if not tem_par:
    print("Nenhum número par foi digitado.")
print()  
