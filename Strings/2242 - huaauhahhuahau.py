risada = input()
vogais_risada = []
cntd = 0
for i in range(len(risada)):
    if risada[i] == "a" or risada[i] == "e" or risada[i] == "i" or risada[i] == "o" or risada[i] == "u":
        vogais_risada.append(risada[i])

for n in range(len(vogais_risada)):
    if vogais_risada[n] != vogais_risada[-1-n]:
        print("N")
        break
    elif vogais_risada[n] == vogais_risada[-1-n]:
        cntd += 1
if cntd == len(vogais_risada):
    print("S")