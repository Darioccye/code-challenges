estacoes, comandos, devastado = map(int, input().split())
com = [int(i) for i in input().split()]

estacao = 1
contador = 0

if estacao == devastado:
    contador += 1
for i in range(comandos):
    if com[i] == 1:
        estacao += 1
    elif com[i] == -1:
        estacao -= 1
    if estacao == 0:
        estacao = estacoes
    if estacao == estacoes+1:
        estacao = 1
    if estacao == devastado:
        contador += 1

print(contador)

