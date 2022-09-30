aaaaaa = input()
bbbbbb = aaaaaa.split()

a = int(bbbbbb[0])
b = int(bbbbbb[1])

hora_comeco = 24 - a


if b > a:
    print("O JOGO DUROU %s HORA(S)" % (b-a))
if a >= b:
    print("O JOGO DUROU %s HORA(S)" % (hora_comeco + b))