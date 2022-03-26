numero_de_casos = int(input())

for n in range(numero_de_casos):
    combinacoes = 1
    senha = input()
    for letra in senha:
        if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'O' or letra == 'o' or letra == 'i' or letra == 'I' or letra == 's' or letra == 'S':
            combinacoes *= 3
        else:
            combinacoes *= 2
    print(combinacoes)

