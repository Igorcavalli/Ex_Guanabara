"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

from datetime import date
ano = date.today().year
Dna = int(input("Informe o ano de nascimento do atleta: "))
categoria = ano - Dna
print(f"Sua idade e {categoria} anos")
if categoria <= 9:
    print(" Sua categoria e MIRIM!")
elif categoria > 9 and categoria <= 14:
    print("Sua categoria e INFANTIL!")
elif categoria > 14 and categoria <=  19:
    print("Sua  categoria e JUNIOR!")
elif categoria > 19 and categoria <= 25:
    print("Sua categoria e SENIOR!")
elif categoria > 25:
    print("Sua  categoria e MASTER")
    