numero = int(input("informe um numero entre zero e 9999: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f"O primeiro numero e: {m}")
print(f"O segundo numero e: {c}")
print(f"O terceiro numero e:{d}")
print(f"o quarto numero e: {u}")
