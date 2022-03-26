import sys

for line in sys.stdin:
    line = int(line)
    arvore = 1
    string_arvore = "*"
    while arvore <= line:
        string_arvore = "*"
        espacamento = ""
        for n in range(1, arvore):
            string_arvore += "*"
        espacos_brancos = int((line-len(string_arvore))/2)
        for n in range(espacos_brancos):
            espacamento += " "
        print("%s%s" % (espacamento, string_arvore))
        arvore += 2
    tronco1 = "*"
    tronco3 = "***"
    espacamento_tronco1 = ""
    espacamento_tronco3 = ""
    espacos_brancos_tronco1 = int((line-len(tronco1))/2)
    espacos_brancos_tronco3 = int((line-len(tronco3))/2)
    for n in range(espacos_brancos_tronco1):
        espacamento_tronco1 += " "
    for n in range(espacos_brancos_tronco3):
        espacamento_tronco3 += " "
    print("%s%s" % (espacamento_tronco1, tronco1))
    print("%s%s" % (espacamento_tronco3, tronco3))
    print()







