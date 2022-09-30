muro = int(input())
subida = int(input())
descida = int(input())

altura = 0
dias = 0

while altura < muro:
    altura += subida
    if altura < muro:
        altura -= descida
    dias += 1

print(dias)