frase = ('curso de análise e desenvolvimento de sistemas')
print(frase[3]) #isso mostra o espaço da memória
print(frase[3:46]) #intervalo de caracteres menos o último
print(frase[3:45:2]) #pula de dois em dois 
print(frase[:5]) #pega do inicio ate o caracter escolhido
print(frase[5:]) #pega do caracter escolhido até o final
print(frase[3::5]) #pega do caracter escolhido pulando de 3 em 3

print(len(frase)) #conta a quantidade de caracteres da memória
print(frase.count('a')) #procura um caracter específico na variavel
print(frase.count('a',3,5)) #procura um caracter específico dentro de um intervalo específico
print(frase.find('urso')) #mostra apartir de qual índice aparece a pesquisa 
print(frase.find('android')) #o resultado -1 indica que não tem essa sequencia na variavel
print('abacate'in frase) #o in verifica se aquele conjunto de string está na variavel