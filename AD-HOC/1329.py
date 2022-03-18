count = int(input())

while count != 0:
    maria = 0
    joao = 0
    jogos = ([int(i) for i in input().split()])
    for i in range(0, count):
        if jogos[i] == 0:
            maria += 1
        if jogos[i] == 1:
            joao += 1
    print("Mary won %s times and John won %s times" % (maria, joao))
    count = int(input())

