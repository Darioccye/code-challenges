a = input()
frase = ""

while a != "":
    frase += a.strip()
    a = input()

print(len(frase))
print(frase)
