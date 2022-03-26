primeiro_numero = int(input())
segundo_numero = int(input())
soma_impares = 0

for n in range(segundo_numero, primeiro_numero):
    if primeiro_numero > n > segundo_numero:
        if n % 2 != 0:
            soma_impares += n

for n in range(primeiro_numero, segundo_numero):
    if segundo_numero > n > primeiro_numero:
        if n % 2 != 0:
            soma_impares += n

print(soma_impares)