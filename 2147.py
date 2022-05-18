numero_de_palavras = int(input())

for n in range(numero_de_palavras):
    galopeira = input()
    tempo_gasto = 0.01*len(galopeira)
    print(format(tempo_gasto, ".2f"))