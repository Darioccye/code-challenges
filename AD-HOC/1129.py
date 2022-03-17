inic = int(input())

while inic != 0:
    for x in range(0, inic):
        alts = ([int(i) for i in input().split()])
        marcas_br = 0
        if alts[0] > 127:
            marcas_br += 1
        if alts[1] > 127:
            marcas_br += 1
        if alts[2] > 127:
            marcas_br += 1
        if alts[3] > 127:
            marcas_br += 1
        if alts[4] > 127:
            marcas_br += 1
        if marcas_br == 4:
            if alts[0] <= 127:
                print("A")
            elif alts[1] <= 127:
                print("B")
            elif alts[2] <= 127:
                print("C")
            elif alts[3] <= 127:
                print("D")
            elif alts[4] <= 127:
                print("E")
        else:
            print("*")
    inic = int(input())
