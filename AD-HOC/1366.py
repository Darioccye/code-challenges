import math
comp_var = int(input())

while comp_var != 0:
    varetas = [input().split() for i in range(0, comp_var)]
    totalx2 = 0
    for i in range(0, comp_var):
        pares = math.floor(int(varetas[i][1])/2)
        for n in range(0, pares):
            totalx2 += 1
    total = math.floor(totalx2/2)
    print(total)

    comp_var = int(input())