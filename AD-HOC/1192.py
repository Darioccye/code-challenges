cas = int(input())

maiusculas = ["A", "B", "C", "D", "E", "F", 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']

while cas > 0:
    a = ' '.join(input())
    b = a.split()
    n1 = int(b[0])
    n2 = int(b[2])
    if n1 == n2:
        print(n1 * n2)
    else:
        if b[1].isupper():
            print(n2 - n1)
        elif b[1].islower():
            print(n1 + n2)
    cas -= 1
