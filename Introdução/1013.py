values = input()
valores = values.split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maiorab = (a+b+abs(a-b))/2
maiorac = (a+c+abs(a-c))/2
maiorbc = (b+c+abs(b-c))/2

if maiorab >= maiorbc:
    print("%s eh o maior" % format(maiorab, ".0f"))
elif maiorbc > maiorab:
    print("%s eh o maior" % format(maiorbc, ".0f"))
