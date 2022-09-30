cifrado = input()
crib = input()

lista_de_cribs = []

posicoes = 0
for i in range(len(cifrado)-len(crib)+1):
    lista_de_cribs.append([crib])
    lista_de_cribs[i] = "a"*i + lista_de_cribs[i][-1]

for i in range((len(cifrado)-len(crib)+1)):
    while len(lista_de_cribs[i]) < len(cifrado):
        lista_de_cribs[i] = lista_de_cribs[i] + "a"

for i in range(len(cifrado):
    if cifrado[i] == lista_de_cribs


print(posicoes)
print(lista_de_cribs)