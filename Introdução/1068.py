numero = int(input())

for n in range(6):
    if numero % 2 == 0:
        prim_impar = numero+1
        print(prim_impar + (n*2))
    if numero % 2 != 0:
        print(numero + (n*2))
