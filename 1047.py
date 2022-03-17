aaaaaa = input()
bbbbbb = aaaaaa.split()

#horas
a = int(bbbbbb[0])
c = int(bbbbbb[2])
#minutos
b = int(bbbbbb[1])
d = int(bbbbbb[3])

hora_comeco = 24 - a
minuto_diferenca = 60-(b-d)


if c > a and d >= b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % ((c-a), (d-b)))
if c > a and d < b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % ((c-a)-1, minuto_diferenca))
if a == c and d == b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (hora_comeco + c, (d-b)))
if a == c and d > b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (0, (d-b)))
if a == c and d < b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % (hora_comeco + c - 1, minuto_diferenca))
if a > c and d >= b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % ((hora_comeco + c), (d-b)))
if a > c and d < b:
    print("O JOGO DUROU %s HORA(S) E %s MINUTO(S)" % ((hora_comeco + c)-1, minuto_diferenca))
