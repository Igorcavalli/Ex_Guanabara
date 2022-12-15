#escreva um programa que leia o valor em metros e retorne o valor digitado em centimetros e milimetros.

un_m = float(input("Informe a medida em metros: "))
m_c = print(f"O valor em cm e: {un_m*100 :.2f} centimetros")
m_mm = print(f"O valor em mm e: {un_m*1000 :.2f} milimetros")
