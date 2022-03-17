tot = input()
numero = tot.split()

code = int(numero[0])
amount = int(numero[1])

if code == 1:
    print("Total: R$ %s" % format((4*amount), ".2f"))
if code == 2:
    print("Total: R$ %s" % format((4.5*amount), ".2f"))
if code == 3:
    print("Total: R$ %s" % format((5*amount), ".2f"))
if code == 4:
    print("Total: R$ %s" % format((2*amount), ".2f"))
if code == 5:
    print("Total: R$ %s" % format((1.5*amount), ".2f"))