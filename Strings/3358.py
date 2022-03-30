quantidade_de_nomes = int(input())

for n in range(quantidade_de_nomes):
    nome = input()
    nome.split()
    dificuldade = 0
    for n in range(len(nome)-2):
        if nome[n] not in 'aeiou' and nome[n+1] not in 'aeiou' and nome[n+2] not in 'aeiou' and nome[n] not in 'AEIOU' and nome[n + 1] not in 'AEIOU' and nome[n + 2] not in 'AEIOU':
            dificuldade += 1
        else:
            dificuldade += 0
    if dificuldade > 0:
        print("%s nao eh facil" % ''.join(nome))
    if dificuldade == 0:
        print("%s eh facil" % ''.join(nome))