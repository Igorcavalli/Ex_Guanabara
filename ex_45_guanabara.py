from random import randint
from time import sleep
print("{:|^50}".format(" JoKenPo "))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print("""
[0] Pedra.
[1] Papel.s
[2] Tesoura.
""")
jogador = int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

print('~'*30)
print(f"O Computador jogou {itens[computador]}")
print(f"O Jogador jogou {itens[jogador]}")
print('~'*30)
sleep(1)

if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("Jogador VENCEU!")
    elif jogador == 2:
        print("Jogador PERDEU!")
elif computador == 1:
    if jogador == 0:
        print("Jogador PERDEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("Jogador VENCEU!")
elif computador == 2:
    if jogador == 0:
        print("Jogador VENCEU!")
    elif jogador == 1:
        print("Jogador PERDEU!")
    elif jogador ==  2:
        print("EMPATE!")
