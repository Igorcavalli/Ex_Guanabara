"""Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente. """

nome = str(input("Informe seu nome: ")).split()

print(f"Seu primrito nome e: {nome[0]}")
print(f"Seu ultimo nome e: {nome[-1]}")
