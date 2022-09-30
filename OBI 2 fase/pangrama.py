a = "a b c d e f g h i j l m n o p q r s t u v x z"
alfabeto = []
for l in a:
    if l != " ":
        alfabeto.append(l)

frase = input()
listfrase = []

for n in frase:
    listfrase.append(n)

for i in listfrase:
    if i in alfabeto:
        alfabeto.remove(i)

if len(alfabeto) == 0:
    print("S")
else:
    print("N")