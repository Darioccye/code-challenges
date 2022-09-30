values = input()
valores = values.split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
pi = 3.14159

rec_tr = (a*c)/2
rad_circ = pi*c**2
trp = ((a+b)/2)*c
sqr = b**2
rect = a*b

print("TRIANGULO: %s" % format(rec_tr, ".3f"))
print("CIRCULO: %s" % format(rad_circ, ".3f"))
print("TRAPEZIO: %s" % format(trp, ".3f"))
print("QUADRADO: %s" % format(sqr, ".3f"))
print("RETANGULO: %s" % format(rect, ".3f"))

