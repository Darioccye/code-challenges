linhas = int(input())
colunas = int(input())

if (linhas + colunas) % 2 == 0:
    print('1')
elif (linhas + colunas) % 2 != 0:
    print('0')