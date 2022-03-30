caso_teste = [int(i) for i in input().split()]

primeiro_numero = caso_teste[0]
segundo_numero = caso_teste[1]

while primeiro_numero != 0 and segundo_numero != 0:
    soma_numeros = primeiro_numero + segundo_numero
    soma_numeros = str(soma_numeros)
    soma_numeros = list(soma_numeros)
    soma_numero_sem_zero = []
    for x in soma_numeros:
        if x != "0":
            soma_numero_sem_zero.append(x)
    print("".join(soma_numero_sem_zero))

    caso_teste = [int(i) for i in input().split()]

    primeiro_numero = caso_teste[0]
    segundo_numero = caso_teste[1]