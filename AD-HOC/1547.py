camisetas = int(input())

for n in range(camisetas):
    alunos_e_numero = [int(i) for i in input().split()]
    alunos = alunos_e_numero[0]
    numero = alunos_e_numero[1]
    ChuteDosAlunos = [int(i) for i in input().split()]
    diferenca = 101
    # numero aleatorio maior do que o limite de chute
    posicao = 0
    for y in range(alunos):
        if ChuteDosAlunos[y] == numero:
            diferenca = (ChuteDosAlunos[y] - numero)
            posicao = y + 1
            break
        elif ChuteDosAlunos[y] > numero and (ChuteDosAlunos[y]-numero) < diferenca:
            diferenca = (ChuteDosAlunos[y]-numero)
            posicao = y+1
        elif ChuteDosAlunos[y] < numero and (numero-ChuteDosAlunos[y]) < diferenca:
            diferenca = (numero-ChuteDosAlunos[y])
            posicao = y+1
    print(posicao)



