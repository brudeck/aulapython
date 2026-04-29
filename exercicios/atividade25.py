from random import randint
from time import sleep
aleatorio = randint(0,5)
print ("vou pensar em um número de 0 a 5. tente adivinhar...")
jogador = int(input("em que número eu pensei"))
print("processando...")
sleep(3)
if aleatorio==jogador:
    print("parabens! voce conseguiu")
else:
    print("ganhei eu pensei no número {} e não o {}".format(aleatorio,jogador))