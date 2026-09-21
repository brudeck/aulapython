def verifica_colchetes(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == '[':
            pilha.append(caractere)  
        elif caractere == ']':
            if not pilha:
                return False  
            pilha.pop()  
            
    return len(pilha) == 0  

testes = ["[a + b]", "[[x * y]]", "[a + b", "a + b]", "]["]

for t in testes:
    resultado = "Correta" if verifica_colchetes(t) else "Incorreta"
    print(f"Expressão: {t} -> {resultado}")
