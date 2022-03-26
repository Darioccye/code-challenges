corr_e_comp = [int(i) for i in input().split()]
corr = corr_e_comp[0]
comp = corr_e_comp[1]

while corr != 0 and comp != 0:
    colocacoes = []
    for x in range(0, corr):
        colocacoes += [int(i) for i in input().split()]
    num_corridas = int(input())
    sist_pont = []

    for m in range(0, num_corridas):
        sist_pont += ([int(i) for i in input().split()])


    corr_e_comp = [int(i) for i in input().split()]
    corr = corr_e_comp[0]
    comp = corr_e_comp[1]

print(colocacoes)
print(sist_pont)



