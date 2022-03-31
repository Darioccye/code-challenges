par = [int(i) for i in input().split()]
primeiro = par[0]
segundo = par[1]

while primeiro > 0 and segundo > 0:
    numeros = []
    soma = 0
    if primeiro >= segundo:
        diferenca = primeiro - segundo
        for n in range(diferenca+1):
            numeros.append(segundo+n)
            soma += segundo+n
    elif segundo >= primeiro:
        diferenca = segundo - primeiro
        for n in range(diferenca+1):
            numeros.append(primeiro+n)
            soma += primeiro+n
    numeros_string = ""
    for n in range(len(numeros)):
        numeros_string += str(numeros[n])
    numeros_string_espacado = " ".join(numeros_string)

    print("%s Sum=%s" % (numeros_string_espacado, soma))
    par = [int(i) for i in input().split()]
    primeiro = par[0]
    segundo = par[1]





