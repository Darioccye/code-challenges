count = int(input())

while count > 0:
    tentativas = int(input())
    ldt = ([int(i) for i in input().split()])
    d = " ".join(input())
    boss = d.split()
    hits = 0
    for i in range(0, tentativas):
        if ldt[i] > 2 and boss[i] == "J":
            hits += 1
        elif ldt[i] <= 2 and boss[i] == "S":
            hits += 1
    print(hits)
    count -= 1
