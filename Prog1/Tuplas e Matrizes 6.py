corredores = []

for i in range(6):
    corredores.append([[input()], [int(i) for i in input().split()]])

tempo_minimo = corredores[0][1][0]
volta = 0
campeao = 0

for n in range(6):
    for i in range(3):
        if corredores[n][1][i] < tempo_minimo:
            tempo_minimo = corredores[n][1][i]
            volta = i
            campeao = n

media = 100000000

for n in range(6):
    media_temp = 0
    for i in range(3):
        media_temp += int(corredores[n][1][i])/3
        if media > media_temp:
            media = media_temp

print(tempo_minimo)
print(corredores[campeao][0])
print(volta+1)
print(media)