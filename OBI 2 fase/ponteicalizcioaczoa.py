qtd = int(input())

soma = 0

for i in range(qtd):
    numero = input()
    potencia = int(numero[-1])
    if len(numero) == 2:
        soma += (int(numero[0])**potencia)
    elif len(numero) == 3:
        soma += (int(numero[0] + numero[1])**potencia)
    elif len(numero) == 4:
        soma += (int(numero[0] + numero[1] + numero[2])**potencia)

print(soma)