matriz_a = [[int(i) for i in input().split()] for linha in range(2)]
matriz_b = [[int(i) for i in input().split()] for linha in range(2)]

matriz_c = []

for n in range(2):
    for i in range(2):
        matriz_a[n][i] += matriz_b[n][i]

matriz_c.append(matriz_a[0])
matriz_c.append(matriz_a[1])

print(matriz_c)
