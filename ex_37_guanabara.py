"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e 
3 para hexadecimal. """

numero = int(input("Digite um numero inteiro "))
print("""

    [1] para Binario.
    [2] para Octal.
    [3] para Hexadecimal.

""")
menu = int(input("Qual sua opcao? "))

if menu == 1:
    print(f"A conversao para Binario e: {bin(numero)[2:]}")
elif menu == 2:
    print(f"A conversao para octal e: {oct(numero)[2:]}")
elif menu  == 3:
    print(f"A conversao para Hexadecimal e: {hex(numero)[2:]}")
else:

    print("Opcao Invalida!")
