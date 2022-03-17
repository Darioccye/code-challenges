import math

a = float(input())

#Notas
n100 = math.floor(a/100)
t100 = n100*100
n50 = math.floor((a-t100)/50)
t50 = t100 + n50*50
n20 = math.floor((a-t50)/20)
t20 = t50 + n20*20
n10 = math.floor((a - t20)/10)
t10 = t20 + n10*10
n5 = math.floor((a - t10)/5)
t5 = t10 + n5*5
n2 = math.floor((a - t5)/2)
t2 = t5 + n2*2

#Moedas
m100 = math.floor(a - t2)
tm1 = t2 + m100*1
m50 = math.floor((a - tm1)/0.5)
tm50 = tm1 + m50*0.5
m25 = math.floor((a - tm50)/0.25)
tm25 = tm50 + m25*0.25
m10 = math.floor((a - tm25)/0.10)
tm10 = tm25 + m10*0.10
m5 = math.floor((a - tm10)/0.05)
tm5 = tm10 + m5*0.05
m1 = round((a-tm5)/0.01)

print("NOTAS:")
print("%s nota(s) de R$ 100.00" % n100)
print("%s nota(s) de R$ 50.00" % n50)
print("%s nota(s) de R$ 20.00" % n20)
print("%s nota(s) de R$ 10.00" % n10)
print("%s nota(s) de R$ 5.00" % n5)
print("%s nota(s) de R$ 2.00" % n2)
print("MOEDAS:")
print("%s moeda(s) de R$ 1.00" % m100)
print("%s moeda(s) de R$ 0.50" % m50)
print("%s moeda(s) de R$ 0.25" % m25)
print("%s moeda(s) de R$ 0.10" % m10)
print("%s moeda(s) de R$ 0.05" % m5)
print("%s moeda(s) de R$ 0.01" % m1)