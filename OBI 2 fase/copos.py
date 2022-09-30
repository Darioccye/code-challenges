acoes = int(input())
letra = input()

pos = 0

if letra == "A":
    pos = 1
if letra == "B":
    pos = 2
if letra == "C":
    pos = 3

lista_acoes = []

for i in range(acoes):
    lista_acoes.append(int(input()))

for i in range(acoes):
    if lista_acoes[i] == 1:
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos = 1
    if lista_acoes[i] == 2:
        if pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2
    if lista_acoes[i] == 3:
        if pos == 3:
            pos = 1
        elif pos == 1:
            pos = 3

if pos == 1:
    print("A")
if pos == 2:
    print("B")
if pos == 3:
    print("C")