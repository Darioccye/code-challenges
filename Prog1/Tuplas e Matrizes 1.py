matriz = [[int(i) for i in input().split()] for lin in range(3)]
multiplicador = int(input())

print(matriz)

for i in range(3):
    matriz[i][i] *= multiplicador

print(matriz)