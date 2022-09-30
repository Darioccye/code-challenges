sal = float(input())

sal8 = (sal-2000)*0.08
sal18 = (sal-3000)*0.18
sal28 = (sal-4500)*0.28

a = sal-1000
b = sal-1500

if 0 < sal <= 2000:
    print("Isento")
if 2000 < sal <= 3000:
    print("R$ %s" % format(sal8, ".2f"))
if 3000 < sal <= 4500:
    sal8 = (sal-a)*0.08
    print("R$ %s" % format((sal8+sal18), ".2f"))
if sal > 4500:
    sal8 = (sal - a) * 0.08
    sal18 = (sal - b)*0.18
    print("R$ %s" % format((sal8+sal18+sal28), ".2f"))