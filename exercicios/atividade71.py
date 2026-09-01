expressao = input("Digite uma expressão com parênteses: ")

pilha = []
valida = True

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')  
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()    
        else:
            valida = False 
            break

if valida and len(pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
