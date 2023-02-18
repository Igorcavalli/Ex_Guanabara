import random
import time
print(" \o/ "*20)
print(f"Vamos brincar de advinhar numero? \n")
print("Vou escolher um numero de zero a 5 e voce tenta advinhar.\n" )
print(" :D "*20)
a=1
b=2
c=3
d=4
e=5
lista = [a,b,c,d,e]

computador = random.choice(lista)

jogador = int(input(f"Escolha um numero entre 1 e 5. \n"))
print("Processando...")
time.sleep(2)
if jogador == computador:
    print("PARABENS Mizeravi, voce acertou!")
else:
    print(f"KKKKK, voce perdeu! eu pensei no numero {computador} \o/")

#pode ser usado o comando randint
#computador = randint(1,5)
