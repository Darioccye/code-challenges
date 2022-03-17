pepega = input()
peepos = pepega.split()

peepog = []
ccc = float(peepos[0])
bbb = float(peepos[1])
aaa = float(peepos[2])

peepog.append(aaa)
peepog.append(bbb)
peepog.append(ccc)

peepog.sort()

c = peepog[0]
b = peepog[1]
a = peepog[2]

impossivel = a >= b+c

if impossivel == True:
    print("NAO FORMA TRIANGULO")
if a**2 == (b**2)+(c**2) and impossivel == False:
    print("TRIANGULO RETANGULO")
if a**2 > (b**2)+(c**2) and impossivel == False:
    print("TRIANGULO OBTUSANGULO")
if a**2 < (b**2)+(c**2) and impossivel == False:
    print("TRIANGULO ACUTANGULO")

if a == b == c and impossivel == False:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c and impossivel == False:
    print("TRIANGULO ISOSCELES")

