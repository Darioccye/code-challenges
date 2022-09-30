lado_verm = int(input(), 16)
lado_verd = int(input(), 16)
lado_azul = int(input(), 16)

etiquetas_verdes = int(lado_verm/lado_verd)
etiquetas_azuis = int(lado_verd/lado_azul)
etiquetas_azuis *= etiquetas_verdes


etiquetas_verdes **= 2
etiquetas_azuis **= 2
et_verm = 1



etiquetas = hex(et_verm + etiquetas_verdes + etiquetas_azuis)
etiquetas = str(etiquetas)

total = etiquetas[2:]
print(total)