pares = 0
for n in range(5):
    numeros = int(input())
    if numeros % 2 == 0:
        pares += 1

print("%s valores pares" % pares)
