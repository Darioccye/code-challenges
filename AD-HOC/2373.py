# Garçom
# Um garçom derruba bandejas se houver mais latas do que copos. A partir disso, faça um programa que conte o numero de
# casos, contendo a quantidade de latas e copos, e imprima quantos copos foram quebrados.

casos = int(input())
copos_quebrados = 0
for n in range(casos):
    latas, copos = map(int, input().split())
    if latas > copos:
        copos_quebrados += copos
print(copos_quebrados)
