ppp = input()
oo = ppp.split()

a = float(oo[0])
b = float(oo[1])
c = float(oo[2])


if abs(b-c) < a < (b+c) and abs(a-b) < c < (a+b) and abs(a-c) < b < (a+c):
    print("Perimetro = %s" % format((a+b+c), ".1f"))
else:
    print("Area = %s" % format(((a+b)*c)/2, ".1f"))
