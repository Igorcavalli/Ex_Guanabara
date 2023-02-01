"""programa para ler nome completo de uma pessoa
    colocar o nome em letras maiusculas
    colocar o nome em letras minusculas
    contar  quantas letras o nome possui sem caracter de espaco
    contar quantas letras possui o primeiro nome"""


nome = str(input("Qual seu nome completo? ")).strip()
print(f"seu nome em letras maiusculas: {nome.upper()}")
print(f"seu  nome em letras minusculas: {nome.lower()}")
print(f"Seu nome possui {(len(nome) - nome.count(' '))} letras")
print(f"Seu primeiro nome tem {nome.find(' ')}")

# utilizou-se o comando .find() para localizar o primeiro cacacter de espaco digitado pelo usuario,
