numeros = []
for n in range(6):
    numeros.append(float(input()))

total = 0
for y in numeros:
    if y > 0:
        total += 1

print("%s valores positivos" % total)