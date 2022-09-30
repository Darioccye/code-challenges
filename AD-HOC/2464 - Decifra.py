permutacao = input()
codigo = input()
codigo_em_num = [[0] * 26 for i in range(len(codigo))]

for i in range(len(codigo)):
    for n in range(26):
        if codigo[i] == chr(97+n):
            codigo_em_num[i][n] += 1

palavra = ""
for i in range(len(codigo_em_num)):
    for n in range(26):
        if codigo_em_num[i][n] == 1:
            palavra += permutacao[n]

print(palavra)