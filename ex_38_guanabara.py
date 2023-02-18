"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

num_1 = int(input("Digite um numero inteiro: "))
num_2 = int(input("Digite um segundo numero Inteiro: "))

if num_1 > num_2:
    print(f"O numero {num_1} e maior que o numero {num_2}!")
elif num_2 > num_1:
    print(f"O numero {num_2} e maior que o numero {num_1}!")
elif num_1 == num_2:
    print(f"Nao existe valor maior, ambos numeros sao iguais!")
