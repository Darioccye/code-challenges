tamanho = int(input())
palavra1 = input()
palavra2 = input()

lista1 = []
lista2 = []

for letra in palavra1:
    if letra != " " and letra != "," and letra != ".":
        lista1.append(letra)

for letra in palavra2:
    if letra != " " and letra != "," and letra != ".":
        lista2.append(letra)

lista1.sort()
lista2.sort()

if lista1 == lista2:
    print("S")
else:
    print("N")