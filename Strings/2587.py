quantidade_de_casos = int(input())

for n in range(quantidade_de_casos):
    primeira_palavra = list(input())
    segunda_palavra = list(input())
    palavra_duvida = list(input())
    letras_em_duvida = []
    for y in range(len(palavra_duvida)):
        if palavra_duvida[y] != primeira_palavra[y]:
            letras_em_duvida.append(primeira_palavra[y])
            letras_em_duvida.append(segunda_palavra[y])
    if letras_em_duvida[0] == letras_em_duvida[3] or letras_em_duvida[1] == letras_em_duvida[2]:
        print("Y")
    elif letras_em_duvida[0] == letras_em_duvida[1] and letras_em_duvida[2] == letras_em_duvida[3]:
        print("Y")
    else:
        print("N")

