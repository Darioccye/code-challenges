# Notas da Prova
# A partir de uma tabela, transformar uma nota de 0 a 100 em uma letra de E a A

nota = int(input())

if nota == 0:
    print("E")
elif nota < 36:
    print("D")
elif nota < 61:
    print("C")
elif nota < 86:
    print("B")
elif nota <= 100:
    print("A")