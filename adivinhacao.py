from random import randint

print("Adivinha um numero entre 0 a 100")
i = randint(0, 100)
a = int(input())
x = 0
b = []
while x != 2:
    if a in b:
        print("Burro pkrl nrml")
    elif a == i:
        print("Parabéns, demorou só 2 horas")
        break
    elif a >= i+20:
        print("Chutou meio alto, hein!")
    elif a <= i-20:
        print("Chutou meio baixo, hein!")
    elif i-5 <= a <= i+5:
        print("Tá perto...")
    elif a != i:
        print("Já foi melhor")
    b.append(a)

    a = int(input())
