import random

numero_computador = random.randint(0, 9)

print("Tente adivinhar o número que eu pensei!")

tentativa_usuario = int(input("Digite um número entre 0 e 9: "))

if tentativa_usuario == numero_computador:
    print(f"Você acertou! Eu pensei no número {numero_computador}.")
    print("O computador PERDEU!")
else:
    print(f"Você errou! Eu pensei no número {numero_computador}.")
    print("O computador GANHOU!")
