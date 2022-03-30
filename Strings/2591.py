casos_teste = int(input())

for n in range(casos_teste):
    hakemaheka = list(input())
    parte1_numero_de_as = 0
    parte2_numero_de_as = 0
    kaaa = "k"
    for x in range(1, len(hakemaheka)-1):
        if hakemaheka[x] == "a":
            parte1_numero_de_as += 1
            if hakemaheka[x+1] == "m":
                parte2_numero_de_as = len(hakemaheka) - parte1_numero_de_as - 6
                break
    total_de_as = parte1_numero_de_as * parte2_numero_de_as
    for x in range(total_de_as):
        kaaa += "a"
    print(kaaa)