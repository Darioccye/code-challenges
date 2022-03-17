name = input()
fixed = float(input())
sold = float(input())

total = fixed + sold*0.15
total = format(total, ".2f")
print("TOTAL = R$ %s" % total)