entradas = int(input())

for n in range(entradas):
    codiguin = input()
    codiguin.split()
    numero1 = ""
    numero2 = ""
    numero3 = ""
    numero1 += codiguin[2]
    numero1 += codiguin[3]
    numero2 += codiguin[5]
    numero2 += codiguin[6]
    numero2 += codiguin[7]
    numero3 += codiguin[11]
    numero3 += codiguin[12]
    soma = int(numero1) + int(numero2) + int(numero3)
    print(soma)