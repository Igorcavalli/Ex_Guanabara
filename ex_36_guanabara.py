"""Exercício Python 36: 
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte
o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
do salário ou então o empréstimo será negado.
"""

casa = float(input("Qual o valor  da casa que deseja financiar? R$ "))
sal = float(input("Informe seu salario: R$ "))
prazo = int(input("Em  quantos anos voce deseja pagar? "))
prestacao = float(f"{casa / (prazo*12):.2f}")
print(f"Sua prestacao e: R$ {prestacao}")
minimo = sal *30/100

if prestacao <= minimo:
    print("Parabens! Voce pode comprar sua casa propria!")
else:
    print("EMPRESTIMO NEGADO!")
    print("Voce precisa de um salario maior ou aumentar o prazo de pagamento") 
