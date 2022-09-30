def baralho(naipe):
    for i in range(13):
        naipe.append(0)

def contagem_baralho(naipe):
    cont = 13
    for i in range(len(naipe)):
        if naipe[i] == 1:
            cont -= 1
        if naipe[i] >= 2:
            print("erro")
            return()
    print(cont)


cartas = input()
numeros = []
naipes = []

for i in range(0, len(cartas), 3):
    cart = cartas[i:i+2]
    numeros.append(int(cart))

for i in range(2, len(cartas), 3):
    nai = cartas[i]
    naipes.append(nai)

paus = []
baralho(paus)
copas = []
baralho(copas)
espadas = []
baralho(espadas)
ouros = []
baralho(ouros)

for i in range(len(naipes)):
    if naipes[i] == "P":
        paus[numeros[i]-1] += 1
    if naipes[i] == "C":
        copas[numeros[i]-1] += 1
    if naipes[i] == "E":
        espadas[numeros[i]-1] += 1
    if naipes[i] == "U":
        ouros[numeros[i]-1] += 1

contagem_baralho(copas)
contagem_baralho(espadas)
contagem_baralho(ouros)
contagem_baralho(paus)

