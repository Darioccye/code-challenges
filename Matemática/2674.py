import sys

for line in sys.stdin:
    aa = line
    decomp = []
    for i in range(len(aa)-1):
        decomp.append(aa[i])
    deco = [int(i) for i in decomp]
    super_primo = True
    for i in deco:
        pri = 0
        for n in range(1, i+1):
            if pri > 2:
                break
            if i % n == 0:
                pri += 1
        if pri > 2 or pri < 2:
            super_primo = False
    line = int(line)
    primos = 0
    for i in range(1, line+1):
        if primos > 2:
            break
        if line % i == 0:
            primos += 1
    if primos == 2:
        if super_primo:
            print("Super")
        else:
            print("Primo")
    if primos < 2 or primos > 2:
        print("Nada")