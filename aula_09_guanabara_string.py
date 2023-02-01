frase = "curso em video python"
print(frase[9]) # imprime a letra na posicao 9

print(frase[9:15]) #imprime o intervalo da string de 9 ate o 15

print(frase[9:21]) #imprime do 9 ao 21, logo ha apenas 20 caracter

print(frase[9:21:2]) #imprime do 9 ao  21 pulando de 2 em 2

print(frase[:5]) #imprime do caracter zero ate o 5, pode escrever assim [0:5]

print(frase[15:]) #imprime do caracter 15 ate o final

print(frase[9::3]) #comecara no caracter 9 e ira pular de 3 em 3

print(len(frase)) #informa a quantidade de caracter

print(frase.count('o',0,14)) #ira mostrar a posicao quea letra O aparece na frase.

print(frase.find('deo')) #procurara a posicao que comeca"deo"

print(frase.find('androide')) #se retornar -1 e pq a string nao aparece

print('curso'in frase) #retorna se existe a palavra frase dentro da string

print(frase.replace('python','androide'))#troca a palavra python por androide
print(frase) 

print(frase.upper()) #todas asletras ficam maiusculas

print(frase.lower()) # todas as letras ficam minusculas

print(frase.capitalize()) #a primeira letras de cada palavra fica em maiuscula

print(frase.title()) #a primeira letra de cada palavra ficara maiuscula

print(frase.strip()) #remove todos os espacos excedentes do inicio e fim da  string 
#pode variar por r.strip(right) ou o l.strip(esquerda)

print(frase.split()) #ira dividir a string em lista palavras onde ha espaco

print("-".join(frase)) # ira separar a frase com tracos




