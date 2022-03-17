values = input()
valores = values.split()

a = float(valores[0])
b = float(valores[1])

if a > 0 and b > 0:
    print("Q1")
elif a < 0 and b > 0:
    print("Q2")
elif a < 0 and b < 0:
    print("Q3")
elif a > 0 and b < 0:
    print("Q4")
elif a != 0 and b == 0:
    print("Eixo X")
elif a == 0 and b != 0:
    print("Eixo Y")
elif a == 0 and b == 0:
    print("Origem")
