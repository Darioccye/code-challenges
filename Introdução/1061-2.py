import math

dia1 = input().split()
hora1= [int(i) for i in input().split(" : ")]
dia2 = input().split()
hora2 = [int(i) for i in input().split(" : ")]

n_dia1 = int(dia1[1])
n_dia2 = int(dia2[1])

d1s = n_dia1*86400
d2s = n_dia2*86400

h1s = hora1[0]*3600
h2s = hora2[0]*3600

m1s = hora1[1]*60
m2s = hora2[1]*60

s1 = hora1[2]
s2 = hora2[2]

total1 = d1s+h1s+m1s+s1
total2 = d2s+h2s+m2s+s2

total = total2-total1

tot_dias = math.floor(total/86400)
tot_horas = math.floor((total-(tot_dias*86400))/3600)
tot_minutos = math.floor((total - (tot_dias*86400) - (tot_horas*3600))/60)
tot_segundos = total - (tot_dias*86400) - (tot_horas*3600) - (tot_minutos*60)

print("%s dia(s)" % tot_dias)
print("%s hora(s)" % tot_horas)
print("%s minuto(s)" % tot_minutos)
print("%s segundo(s)" % tot_segundos)
