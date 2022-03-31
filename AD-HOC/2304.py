inicial_e_operacoes = [int(i) for i in input().split()]
valor_inicial = inicial_e_operacoes[0]
num_operacoes = inicial_e_operacoes[1]

Dalia = valor_inicial
Eloi = valor_inicial
Felix = valor_inicial

for n in range(num_operacoes):
    operacao = input().split()
    if operacao[0] == "C":
        if operacao[1] == "D":
            Dalia -= int(operacao[2])
        if operacao[1] == "E":
            Eloi -= int(operacao[2])
        if operacao[1] == "F":
            Felix -= int(operacao[2])
    if operacao[0] == "V":
        if operacao[1] == "D":
            Dalia += int(operacao[2])
        if operacao[1] == "E":
            Eloi += int(operacao[2])
        if operacao[1] == "F":
            Felix += int(operacao[2])
    if operacao[0] == "A":
        if operacao[1] == "D":
            if operacao[2] == "E":
                Dalia += int(operacao[3])
                Eloi -= int(operacao[3])
            if operacao[2] == "F":
                Dalia += int(operacao[3])
                Felix -= int(operacao[3])
        if operacao[1] == "E":
            if operacao[2] == "D":
                Eloi += int(operacao[3])
                Dalia -= int(operacao[3])
            if operacao[2] == "F":
                Eloi += int(operacao[3])
                Felix -= int(operacao[3])
        if operacao[1] == "F":
            if operacao[2] == "D":
                Felix += int(operacao[3])
                Dalia -= int(operacao[3])
            if operacao[2] == "E":
                Felix += int(operacao[3])
                Eloi -= int(operacao[3])
print("%s %s %s" % (Dalia, Eloi, Felix))

