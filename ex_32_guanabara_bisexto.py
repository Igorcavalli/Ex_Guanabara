"""Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import date
print("Quer saber se um ano e Bisexto?")

ano = int(input(f"Digite o ano: ou {1}para o ano atual: "))

if ano == 1:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f"O ano de {ano} e bissexto!")
else:
    print(f"o ano de {ano} nao e bissexto")
