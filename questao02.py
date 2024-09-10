# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

string = input("Digite uma string qualquer: ").lower()
letra = 'a'

contagem = string.count(letra)

if contagem > 0:
    print(f"A letra {letra} aparece {contagem} vezes na string")
else:
    print(f"A letra {letra} não aparece na string")
