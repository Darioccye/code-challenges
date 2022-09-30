quantidade_de_numeros = int(input())

dentro_do_intervalo = 0
fora_do_intervalo = 0

for n in range(quantidade_de_numeros):
    numero = int(input())
    if 10 <= numero <= 20:
        dentro_do_intervalo += 1
    else:
        fora_do_intervalo += 1

print("%s in" % dentro_do_intervalo)
print("%s out" % fora_do_intervalo)
