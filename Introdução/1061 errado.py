dia1 = input().split()
hora1= [int(i) for i in input().split(" : ")]
dia2 = input().split()
hora2 = [int(i) for i in input().split(" : ")]

n_dia1 = int(dia1[1])
n_dia2 = int(dia2[1])
#dias
dif_dia = n_dia2 - n_dia1
if n_dia1 < n_dia2:
    if hora1[0] <= hora2[0]:
        print('%s dia(s)' % dif_dia)
    elif hora1[0] > hora2[0]:
        print('%s dia(s)' % (dif_dia - 1))
if n_dia1 == n_dia2:
    print("0 dia(s)")

#horas
if hora1[0] < hora2[0]:
    dif_hora = hora2[0] - hora1[0]
    if hora1[1] <= hora2[1]:
        print('%s hora(s)' % dif_hora)
    elif hora1[1] > hora2[1]:
        print('%s hora(s)' % (dif_hora-1))
if hora1[0] > hora2[0]:
    dh = 24 - (hora1[0] - hora2[0])
    if hora1[1] <= hora2[1]:
        print('%s hora(s)' % dh)
    elif hora1[1] > hora2[1]:
        print('%s hora(s)' % (dh-1))
if hora1[0] == hora2[0]:
    print("0 hora(s)")

#minutos
if hora1[1] < hora2[1]:
    dif_min = hora2[1] - hora1[1]
    if hora1[2] <= hora2[2]:
        print('%s minuto(s)' % dif_min)
    elif hora1[2] > hora2[2]:
        print('%s minuto(s)' % (dif_min-1))
if hora1[1] > hora2[1]:
    dm = 60 - (hora1[1] - hora2[1])
    if hora1[2] <= hora2[2]:
        print('%s minuto(s)' % dm)
    elif hora1[2] > hora2[2]:
        print('%s minuto(s)' % (dm-1))
if hora1[1] == hora2[1]:
    print("0 minuto(s)")

#segundos
if hora1[2] > hora2[2]:
    print("%s segundo(s)" % (60 - (hora1[2] - hora2[2])))
elif hora1[2] <= hora2[2]:
    print("%s segundo(s)" % (hora2[2]- hora1[2]))
