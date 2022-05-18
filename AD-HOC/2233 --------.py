hex_vermelho = (int(input(), 16))**2
hex_verde = (int(input(), 16))**2
hex_azul = (int(input(), 16))**2

qtd_verdes = hex_vermelho//hex_verde
qtd_azul = ((qtd_verdes*hex_verde)//hex_azul)

qtd_total = hex(qtd_azul+qtd_verdes+1)[2:]
print(qtd_total)