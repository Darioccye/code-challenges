numero = int(input())
tabuada = []

for n in range(1, 11):
    tabuada.append(numero*n)

multiplicador = 1
for y in range(10):
    print("%s x %s = %s" % (multiplicador, numero, tabuada[y]))
    multiplicador += 1

