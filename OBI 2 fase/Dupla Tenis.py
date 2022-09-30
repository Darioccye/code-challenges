A = int(input())
B = int(input())
C = int(input())
D = int(input())

lista_num = [A, B, C, D]
lista_num.sort()
soma1 = lista_num[0] + lista_num[3]
soma2 = lista_num[1] + lista_num[2]

diferenca = (((soma2 - soma1)**2)**0.5)
print(format(diferenca, ".0f"))