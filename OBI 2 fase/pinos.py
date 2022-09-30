def pivo_linha(lin):
    contador = 0
    for i in range(5):
        if lin[i] == "o" and lin[i+1] == "o" and lin[i+2] == ".":
            contador += 1
    for i in range(6, 1, -1):
        if lin[i] == "o" and lin[i-1] == "o" and lin[i-2] == ".":
            contador += 1
    return contador

def pivo_coluna(col):
    contador = 0
    for i in range(5):
        if col[i] == "o" and col[i+1] == "o" and col[i+2] == ".":
            contador += 1
    for i in range(6, 1, -1):
        if col[i] == "o" and col[i-1] == "o" and col[i-2] == ".":
            contador += 1
    return contador

linhas = []
for i in range(7):
    linhas.append(input())

colunas = [""]*7
for i in range(7):
    for n in range(7):
        colunas[i] += linhas[n][i]

jogadas = 0
for i in range(7):
    jogadas += pivo_linha(linhas[i])
    jogadas += pivo_coluna(colunas[i])


print(jogadas)