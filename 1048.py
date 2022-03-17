valor = float(input())

valor15 = valor*1.15
valor12 = valor*1.12
valor10 = valor*1.10
valor7 = valor*1.07
valor4 = valor*1.04

general = """Novo salario: %s
Reajuste ganho: %s
Em percentual: %s"""


if 2000 < valor:
    print(general % (format(valor4, ".2f"), format(valor4-valor, ".2f"), "4 %"))
elif 1200 < valor <= 2000:
    print(general % (format(valor7, ".2f"), format(valor7-valor, ".2f"), "7 %"))
elif 800 < valor <= 1200:
    print(general % (format(valor10, ".2f"), format(valor10-valor, ".2f"), "10 %"))
elif 400 < valor <= 800:
    print(general % (format(valor12, ".2f"), format(valor12-valor, ".2f"), "12 %"))
elif 0 <= valor <= 400:
    print(general % (format(valor15, ".2f"), format(valor15-valor, ".2f"), "15 %"))
