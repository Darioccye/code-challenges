campeonato = [int(i) for i in input().split()]

jogos = campeonato[0]
pontos = campeonato[1]
vitorias = campeonato[2]
pontos_vit = vitorias*3
empates = campeonato[3]
derrota = campeonato[4]

if derrota == -1:
    if pontos == -1:
        pontos = pontos_vit + empates
    if vitorias == -1:
        vitorias = int((pontos - empates) / 3)
    if empates == -1:
        empates = pontos - pontos_vit
    derrota = jogos - empates - vitorias
elif pontos == -1:
    if jogos == -1:
        jogos = vitorias + empates + derrota
    if vitorias == -1:
        vitorias = jogos - empates - derrota
    if empates == -1:
        empates = jogos - vitorias - derrota
    if derrota == -1:
        derrota = jogos - empates - vitorias
    pontos = pontos_vit + empates
elif jogos == -1:
    if vitorias == -1:
        vitorias = int((pontos - empates)/3)
    if pontos == -1:
        pontos = pontos_vit + empates
    if empates == -1:
        empates = pontos - pontos_vit
    jogos = vitorias + empates + derrota
elif vitorias == -1:
    if empates == -1:
        empates = pontos - pontos_vit
    if jogos == -1:
        jogos = vitorias + empates + derrota
    if pontos == -1:
        pontos = pontos_vit + empates
    vitorias = int((pontos - empates)/3)

if empates == -1:
    empates = pontos - pontos_vit


print(jogos, pontos, vitorias, empates, derrota)