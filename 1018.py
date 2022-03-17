import math

a = int(input())

n100 = math.floor(a/100)
n50 = math.floor((a-n100*100)/50)
n20 = math.floor((a-((n100*100) + n50*50))/20)
n10 = math.floor((a - ((n100*100) + (n50*50) + (n20*20)))/10)
n5 = math.floor((a - ((n100*100) + (n50*50) + (n20*20) + (n10*10)))/5)
n2 = math.floor((a - ((n100*100) + (n50*50) + (n20*20) + (n10*10) + (n5*5)))/2)
n1 = math.floor((a - ((n100*100) + (n50*50) + (n20*20) + (n10*10) + (n5*5) + (n2*2))))

print(a)
print("%s nota(s) de R$ 100,00" % n100)
print("%s nota(s) de R$ 50,00" % n50)
print("%s nota(s) de R$ 20,00" % n20)
print("%s nota(s) de R$ 10,00" % n10)
print("%s nota(s) de R$ 5,00" % n5)
print("%s nota(s) de R$ 2,00" % n2)
print("%s nota(s) de R$ 1,00" % n1)
