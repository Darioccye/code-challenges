postos, competidores, checagens = map(int, input().split())
posicoes = []

for i in range(checagens):
    posicoes.append([int(i) for i in input().split()])

for i in range(len(posicoes)):
