horizontal = input()
vertical = input()

indices_hor = []
indices_ver = []

for i in range(len(horizontal)):
    for n in range(len(vertical)):
        if horizontal[i] == vertical[n]:
            indices_hor.append(i+1)
            indices_ver.append(n+1)

if len(indices_hor) != 0:
    print(indices_hor[-1], indices_ver[-1])
else:
    print("-1 -1")