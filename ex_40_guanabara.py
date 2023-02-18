"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
media = float(f"{(nota_1 + nota_2)/2:.2f}")

if media < 5.0:
    print(f"Sua media foi {media}, voce esta REPROVADO!")
elif media >= 5.0 and media <= 6.9:
    print(f"Sua media foi {media}, Voce esta em RECUPERACAO!")
elif media >= 7.0:
    print(f"Sua media e {media}, voce foi APROVADO!")
