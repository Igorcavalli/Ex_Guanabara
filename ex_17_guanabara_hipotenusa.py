import math
'''print("Vamos calcular a Hipotenusa do Triangulo Retangulo?")
co = float(input('Digite o Cateto Oposto: '))
ca = float(input("Digite o Cateto Adjacente: "))
h = (f'{math.sqrt((ca**2) + (co**2)):.0f}')
print(f"A hipotenusa vale {h}")'''

print("Vamos calcular a Hipotenusa do Triangulo Retangulo?")
co = float(input('Digite o Cateto Oposto: '))
ca = float(input("Digite o Cateto Adjacente: "))
h = math.hypot(co, ca)
print(f'A Hipotenusa vale {h:.0f}')
