values = input()
valores = values.split()

geral = []
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

geral.append(a)
geral.append(b)
geral.append(c)

geral_std = sorted(geral)

sorting = """%s
%s
%s

%s
%s
%s""" % (geral_std[0], geral_std[1], geral_std[2], geral[0], geral[1], geral[2])

print(sorting)
