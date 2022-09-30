estados = int(input())
lista_estados = []

for n in range(estados):
    tabela = input().split()
    estado = tabela[0]
    alcool = float(tabela[1])
    gasosa = float(tabela[2])
    if (gasosa*0.7) >= alcool:
        lista_estados.append(estado)

for i in lista_estados:
    print(i)
if len(lista_estados) == 0:
    print("*")
