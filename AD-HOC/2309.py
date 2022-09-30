rodadas = int(input())
rodadas_adalberto = 0
rodadas_bernadete = 0

for i in range(rodadas):
    cartas = [int(a) for a in input().split()]
    for n in range(6):
        if cartas[n] == 2:
            cartas[n] += 13
        elif cartas[n] == 3:
            cartas[n] += 13
        elif cartas[n] == 1:
            cartas[n] += 13
        elif cartas[n] == 11:
            cartas[n] += 1
        elif cartas[n] == 12:
            cartas[n] -= 1
    adalberto = 0
    bernadete = 0
    if cartas[0] > cartas[3]:
        adalberto += 1
    if cartas[0] < cartas[3]:
        bernadete += 1
    if cartas[1] > cartas[4]:
        adalberto += 1
    if cartas[1] < cartas[4]:
        bernadete += 1
    if cartas[2] > cartas[5]:
        adalberto += 1
    if cartas[2] < cartas[5]:
        bernadete += 1
    if adalberto >= bernadete:
        rodadas_adalberto += 1
    elif adalberto < bernadete:
        rodadas_bernadete += 1
print(rodadas_adalberto, rodadas_bernadete)
