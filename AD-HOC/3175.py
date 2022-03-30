quantidade_de_criancas = int(input())
atos_bons = [int(i) for i in input().split()]

contagem = dict()
for i in atos_bons:
    contagem[i] = contagem.get(i, 0) + 1
presentes_por_crianca = 1
total_de_presentes = 0
atos_bons_sem_repeticao = []
for n in atos_bons:
    if n not in atos_bons_sem_repeticao:
        atos_bons_sem_repeticao.append(n)

atos_bons_sem_repeticao.sort()

for n in atos_bons_sem_repeticao:
    if n in contagem:
        total_de_presentes += presentes_por_crianca*contagem[n]
        presentes_por_crianca += 1

print(total_de_presentes)
