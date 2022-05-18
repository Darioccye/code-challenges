numeros = [int(i) for i in input().split()]

dividido = numeros[0]
divisor = numeros[1]

if dividido < 0 and divisor > 0:
    dividido = -1*dividido
    quociente = int(dividido/divisor)
    if dividido > (quociente*divisor):
        quociente += 1
        resto = (quociente*divisor)-dividido
        print((-1*quociente), resto)
    else:
        resto = (quociente * divisor) - dividido
        print((-1*quociente), resto)
elif dividido < 0 and divisor < 0:
    quociente2 = int(dividido/divisor)
    if dividido < (quociente2*divisor):
        quociente2 += 1
        resto2 = dividido-(quociente2*divisor)
        print(quociente2, resto2)
    else:
        resto2 = dividido - (quociente2 * divisor)
        print(quociente2, resto2)
else:
    quociente = int(dividido/divisor)
    resto = dividido-(quociente*divisor)
    print(quociente, resto)
