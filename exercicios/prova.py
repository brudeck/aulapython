contador = 0
produto = 1

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero == 757:
       
        contador += 1
        produto *= 757
        break
        
    contador += 1
    produto *= numero

print(f"\nQuantidade de números digitados: {contador}")
print(f"Resultado da multiplicação: {produto}")
