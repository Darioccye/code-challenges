testes = int(input())

for i in range(testes):
    A, B = map(str, input().split())
    cont = 0
    if len(A) >= len(B):
        for n in range(len(B)):
            if B[n] == A[-len(B)+n]:
                cont += 1
        if cont == len(B):
            print('encaixa')
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
