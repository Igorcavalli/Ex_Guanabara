"""Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
ano = date.today().year
nascimento = int(input("Qual ano voce nasceu: "))
idade = ano - nascimento
if idade == 18:
    print("Voce esta no ano de alistar-se!")
elif idade < 18:
    print(f"anida faltam {18 - idade} anos para voce alistar-se!")
else:
    print(f"Voce ja passou daidade de alistamento, esta {idade - 18} anos atrasado!")
