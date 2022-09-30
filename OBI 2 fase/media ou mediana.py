def media(n1, n2, n3):
    med = (n1+n2+n3)/3
    return med

def mediana(n1, n2, n3):
    lista = [n1, n2, n3]
    lista.sort()
    med = lista[1]
    return med

A, B = map(int, input().split())

listanum = [A, B]
D = listanum[1]

for i in range(-D, D):
    if media(A, B, i) == mediana(A, B, i):
        print(i)
        break


