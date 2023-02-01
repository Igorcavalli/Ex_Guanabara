import random

a = input("primeiro nome: ")
b = input("segundo nome: ")
c = input("terceiro nome: ")
d = input("Quarto nome: ")
e = input('Quinto nome: ')
f = input("sexto nome: ")

lista = [a, b, c, d, e, f]

random.shuffle(lista)
print(lista)

