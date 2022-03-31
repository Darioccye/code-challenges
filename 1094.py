experimentos = int(input())

total = 0
coelhos = 0
sapos = 0
ratos = 0

for n in range(experimentos):
    numero_e_cobaia = input().split()
    numero = int(numero_e_cobaia[0])
    cobaia = numero_e_cobaia[1]
    if cobaia == "C":
        coelhos += numero
        total += numero
    elif cobaia == "S":
        sapos += numero
        total += numero
    elif cobaia == "R":
        ratos += numero
        total += numero

percentual_coelhos = format(float(coelhos*100/total), ".2f")
percentual_ratos = format(float(ratos*100/total), ".2f")
percentual_sapos = format(float(sapos*100/total), ".2f")

print("Total: %s cobaias" % total)
print("Total de coelhos: %s" % coelhos)
print("Total de ratos: %s" % ratos)
print("Total de sapos: %s" % sapos)
print("Percentual de coelhos: %s %s" % (percentual_coelhos, "%"))
print("Percentual de ratos: %s %s" % (percentual_ratos, "%"))
print("Percentual de sapos: %s %s" % (percentual_sapos, "%"))