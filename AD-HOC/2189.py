participantes = int(input())
num_teste = 1

while participantes != 0:
    print("Teste", num_teste)
    ingresso = [int(i) for i in input().split()]
    for i in range(1, participantes+1):
        if ingresso[i-1] == i:
            print(i)
            print()
    num_teste += 1
    participantes = int(input())
