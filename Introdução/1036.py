def bhaskara1(aa, bb, cc):
    delta = bb**2 - (4*aa*cc)
    if aa == 0 or delta <= 0:
        return "str"
    else:
        bhask1 = (-bb + (delta ** 0.5)) / (2 * aa)
        return bhask1

def bhaskara2(aa, bb, cc):
    delta = bb**2 - (4*aa*cc)
    if aa == 0 or delta <= 0:
        return "str"
    else:
        bhask2 = (-bb - delta ** 0.5) / (2 * aa)
        return bhask2

values = input()
valores = values.split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

R1 = bhaskara1(a, b, c)
R2 = bhaskara2(a, b, c)


if not isinstance(R1, float):
    print("Impossivel calcular")
else:
    print("R1 = %s" % format(bhaskara1(a, b, c), ".5f"))

if isinstance(R2, float):
    print("R2 = %s" % format(bhaskara2(a, b, c), ".5f"))



# Problemas com x = 0

