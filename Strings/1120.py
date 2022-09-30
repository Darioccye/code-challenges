faltando, numero = map(str, input().split())

while faltando != "0" and numero != "0":
    lista_numero = []
    for i in range(len(numero)):
        lista_numero.append(numero[i])
    for i in range(len(lista_numero)-1, -1, -1):
        if lista_numero[i] == faltando:
            lista_numero.pop(i)
    while True:
        if len(lista_numero) == 0:
            break
        for i in range(1):
            if lista_numero[i] == "0" and len(lista_numero) > 1:
                lista_numero.remove(lista_numero[i])
        if lista_numero[0] != "0":
            break
        elif lista_numero[0] == "0" and len(lista_numero) == 1:
            break
    if len(lista_numero) != 0:
        print("".join(lista_numero))
    elif len(lista_numero) == 0:
        print(0)
    faltando, numero = map(str, input().split())
