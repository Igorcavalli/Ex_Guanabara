"""Exercício Python 26: Faça um programa que leia uma frase pelo teclado 
e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a
primeira vez e em que posição ela aparece a última vez."""

frase = str(input("Digite uma frase: \n")).upper().strip()
a = frase.count("A")
print(f"A letra A aparece {a} vezes na frase digitada \n")
print(f"A primeira letra apareceu na posicao {frase.find('A') +1}\n")
print(f"A ultima letra A apareceu na posicao {frase.rfind('A') +1}\n")
