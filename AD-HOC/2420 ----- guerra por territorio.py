num_ter = int(input())
territorios = [int(i) for i in input().split()]

direita = territorios[0]
esquerda = 0
ind_direita = 1
ind_esquerda = len(territorios)-1


while direita != esquerda or ind_direita-1 != ind_esquerda:
    if direita <= esquerda:
        direita += territorios[ind_direita]
        ind_direita += 1
    elif esquerda < direita:
        esquerda += territorios[ind_esquerda]
        ind_esquerda -= 1

print(ind_direita)

# while ind_direita+(ind_esquerda-len(territorios)) != len(territorios):
# while direita != esquerda:
