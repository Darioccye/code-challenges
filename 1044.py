qqq = input()
bbb = qqq.split()

a = int(bbb[0])
b = int(bbb[1])

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

