numero = int(input())

for n in range(1, numero+1):
    if n % 2 == 0:
        print("%s^2 = %s" % (n, n**2))
