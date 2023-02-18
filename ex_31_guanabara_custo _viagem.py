""" Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
    parta viagens mais longas."""

v = float(input("Qual distancia percorrera na sua viagem? "))
a = 0.50
b = 0.45
if v <= 200:
    print(f"Sua viagem custara R$ {v * a :.2f}")
else:
    print(f"Sua viagem custara R$ {v * b :.2f}")
