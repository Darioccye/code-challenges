kung = int(input())
lu = int(input())

final = [0]
semi = [0]*2
quartas = [0]*4
oitavas = [0]*8

for i in range(1, 16, 2):
    if lu == i or lu == i+1:
        oitavas[int(i/2)] += 1
    if kung == i or kung == i+1:
        oitavas[int(i/2)] += 1

if 2 in oitavas:
    print('oitavas')
else:
    for i in range(8):
        if oitavas[i] == 1:
            quartas[int(i/2)] += 1

if 2 in quartas:
    print('quartas')
else:
    for i in range(4):
        if quartas[i] == 1:
            semi[int(i/2)] += 1

if 2 in semi:
    print('semifinal')

if 2 not in oitavas and 2 not in quartas and 2 not in semi:
    print('final')
