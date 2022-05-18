# Overflow
# Dado um valor x, faça um programa que calcule se a operação de dois valores ultrapassa x

maximo = int(input())
operacao = input().split()

valor1 = int(operacao[0])
sinal = operacao[1]
valor2 = int(operacao[2])

if sinal == "+":
    if valor1 + valor2 > maximo:
        print("OVERFLOW")
    else:
        print("OK")
if sinal == "*":
    if valor1 * valor2 > maximo:
        print("OVERFLOW")
    else:
        print("OK")