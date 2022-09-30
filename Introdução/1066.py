pares = 0
impares = 0
positivos = 0
negativos = 0
for n in range(5):
    numero = int(input())
    if numero % 2 != 0:
        impares += 1
    if numero % 2 == 0:
        pares += 1
    if numero > 0:
        positivos += 1
    if numero < 0:
        negativos += 1

print("%s valor(es) par(es)" % pares)
print("%s valor(es) impar(es)" % impares)
print("%s valor(es) positivo(s)" % positivos)
print("%s valor(es) negativo(s)" % negativos)
