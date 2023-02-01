import random

a1 = str(input("Primeiro aluno: ")).upper()
a2 =str(input("Segundo aluno: ")).upper()
a3 = str(input("terceiro auluno ")).upper()
a4 = str(input("quarto aluno ")).upper()

lista =[a1, a2, a3, a4]

escolhido = random.choices(lista)

print(f"O aluno escolhido foi: {escolhido}")
