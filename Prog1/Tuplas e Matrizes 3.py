linhas_a = int(input())
colunas_a = int(input())
linhas_b = int(input())
colunas_b = int(input())

matriz_a = [[int(i) for i in input().split()] for lin in range(linhas_a)]
matriz_b = [[int(i) for i in input().split()] for lin in range(linhas_b)]

print(matriz_a)
print(matriz_b)

if linhas_a == linhas_b and colunas_a == colunas_b:
    for i in range(linhas_a):
        for n in range(colunas_a):
            matriz_a[i][n] *= matriz_b[i][n]
    print(matriz_a)
    