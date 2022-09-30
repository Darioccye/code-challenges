intros = int(input())

while intros != 0:
    cartas = [int(i) for i in input().split()]
    maior = 0
    for i in range(cartas[0]+1, -1, -1):
        if cartas[0] % i == 0 and cartas[1] % i == 0:
            maior = i
            break
    print(maior)
    intros -= 1