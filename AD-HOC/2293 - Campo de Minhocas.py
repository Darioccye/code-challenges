linha, coluna = map(int, input().split())
campo = []

for n in range(linha):
    campo.append([int(i) for i in input().split()])

minhocas_dos_campos = []
for i in range(linha):
    minhocas_dos_campos.append(sum(campo[i]))

for i in range(coluna):
    soma = 0
    for n in range(linha):
        soma += campo[n][i]
    minhocas_dos_campos.append(soma)
    soma = 0

minhocas_dos_campos.sort()
print(minhocas_dos_campos[-1])

