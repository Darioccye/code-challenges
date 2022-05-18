#media = a+b+c/3 = x
#mediana = media = x
#Considerando a = o menor numero do input
#media = a = x
#a+b+c = 3a :    c = 2a-b

AB = [int(i) for i in input().split()]
AB.sort()
A = AB[0]
B = AB[1]

while A != 0 and B != 0:
    C = (2*A)-B
    print(C)
    AB = [int(i) for i in input().split()]
    AB.sort()
    A = AB[0]
    B = AB[1]


