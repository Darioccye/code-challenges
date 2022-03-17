a = float(input())

if 25 >= a >= 0:
    print("Intervalo [0,25]")

if 50 >= a > 25:
    print("Intervalo (25,50]")

if 75 >= a > 50:
    print("Intervalo (50,75]")

if 100 >= a > 75:
    print("Intervalo (75,100]")

if a < 0:
    print("Fora de intervalo")

if a > 100:
    print("Fora de intervalo")