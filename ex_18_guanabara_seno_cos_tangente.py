import math
a = float(input("informe o angulo a ser calculado: "))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print("O angulo de {} tem Seno de {:.2f}".format(a,seno))
print("O angulo de {} tem Cosseno de {:.2f}".format(a,cos))
print(f"O angulo de {a} tem tangente de {tg:.2f}")

# os angulos sao apresentados em radianos, precisa converter usando math.radians
