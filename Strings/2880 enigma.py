cifrado = input()
crib = input()

posicoes = 0

for i in range(len(cifrado)-len(crib)+1):
    checker = 0
    for n in range(len(crib)):
        if cifrado[n+i] == crib[n]:
            checker += 1
            break
    if checker == 0:
        posicoes += 1



print(posicoes)