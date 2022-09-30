matriz = [[int(i) for i in input().split()] for linha in range(3)]

linha1 = 0
linha2 = 0
linha3 = 0

for n in range(3):
    linha1 += matriz[0][n]
    linha2 += matriz[1][n]
    linha3 += matriz[2][n]

print(matriz)
if linha1 > linha2 and linha1 > linha3:
    print(matriz[0])
    print(linha1)
elif linha2 > linha1 and linha2 > linha3:
    print(matriz[1])
    print(linha2)
elif linha3 > linha1 and linha3 > linha2:
    print(matriz[2])
    print(linha3)


