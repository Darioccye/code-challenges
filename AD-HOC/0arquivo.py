import random
aaa = open("0 nomes.py")
bbb = open("0 sobrenomes.py")
ccc = open("0arquivoteste.py", "w")
a = aaa.readlines()
b = bbb.readlines()

vn = []
vs = []

for i in range(len(a)):
    x = random.randint(0, 4)
    n = a[x]
    y = random.randint(0, 4)
    s = b[y]
    z = random.randint(0, 100)
    while x in vn:
        x = random.randint(0, 4)
        n = a[x]
    vn.append(x)
    while y in vs:
        y = random.randint(0, 4)
        s = b[y]
    vs.append(y)
    nome = n.strip()
    sobre = s.strip()
    ccc.write(nome + " " + sobre + ", " + str(z) + "\n")

aaa.close()
bbb.close()
ccc.close()