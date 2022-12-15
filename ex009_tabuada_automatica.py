#informe um  numero que te informarei a tabuada dele.

a = int(input("Digite um numero (multiplicando) para ver sua tabuada. "))
b = int(input("informe ate qual o multiplicador ? "))
contador = 0

while contador <= b:
    print(f" {a} x {contador:2} = {contador*a:2}") 
    contador += 1 
    