lista = [1, 2, 3]

string = ""

for n in range(len(lista)):
    string += str(lista[n])

a = " ".join(string)
print(a)