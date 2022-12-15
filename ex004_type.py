# informe o tipo do que foi digitado.

a = input("Digite algo: ")
print("O que foi digitado e:", type(a))
print("tem espaco?:", a.isspace())
print("tem numeros?", a.isdecimal())
print("e alfanumerico? ", a.isalnum())
