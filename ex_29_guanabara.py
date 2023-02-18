"""Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

vel = float(input("Velocidade do veiculo: "))
multa = (float(vel-80)*7)
if vel >= 80.0:
    print("Voce excedeu a velocidade e foi multado")
    (print(f"Sua multa e de R$ {multa:.2f}"))
else:
    print("tenha um bom dia, dirija com seguranca!")
