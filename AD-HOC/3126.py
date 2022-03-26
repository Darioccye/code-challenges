candidatos = int(input())

presenca = [int(i) for i in input().split()]
total = 0
for x in range(0, len(presenca)):
    if presenca[x] == 1:
        total += 1
print(total)