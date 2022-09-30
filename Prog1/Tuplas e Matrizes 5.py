ordem = int(input())

matriz = [[int(i) for i in input().split()] for linha in range(ordem)]
matriz_transposta = [[0] * ordem for lin in range(ordem)]

for i in range(ordem):
    for n in range(ordem):
        matriz_transposta[i][n] = matriz[n][i]

print(matriz_transposta)

