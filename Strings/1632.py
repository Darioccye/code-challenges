numero_de_casos = int(input())

for n in range(numero_de_casos):
    combinacoes = 1
    senha = input()
    for letra in senha:
        if letra in 'aeios' or letra in 'AEIOS':
            combinacoes *= 3
        else:
            combinacoes *= 2
    print(combinacoes)

