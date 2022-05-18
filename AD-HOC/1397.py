rodadas = int(input())

while rodadas != 0:
    og = 0
    filho = 0
    for n in range(rodadas):
        num_og, num_filho = map(int, input().split())
        if num_og > num_filho:
            og += 1
        elif num_filho > num_og:
            filho += 1
    print(og, filho)
    rodadas = int(input())