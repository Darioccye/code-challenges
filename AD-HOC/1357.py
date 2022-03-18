def brai(x):
    braille_inicio.append(braille[x][0])
    braille_meio.append(braille[x][1])
    braille_final.append(braille[x][2])


braille = (['.*', '**', '..'], ["*.", "..", ".."], ['*.', '*.', '..'], ['**', '..', '..'], ['**', '.*', '..'], ['*.', '.*', '..'], ['**', '*.', '..'],
           ['**', '**', '..'], ['*.', '**', '..'], ['.*', '*.', '..'])

amount = int(input())

while amount != 0:
    letter = input()
    if letter == "S":
        n = input()
        m = " ".join(n)
        nmbrs = [int(i) for i in m.split()]
        braille_inicio = []
        braille_meio = []
        braille_final = []
        for x in nmbrs:
            if x == 0:
                brai(0)
            elif x == 1:
                brai(1)
            elif x == 2:
                brai(2)
            elif x == 3:
                brai(3)
            elif x == 4:
                brai(4)
            elif x == 5:
                brai(5)
            elif x == 6:
                brai(6)
            elif x == 7:
                brai(7)
            elif x == 8:
                brai(8)
            elif x == 9:
                brai(9)
        print(" ".join(braille_inicio))
        print(" ".join(braille_meio))
        print(" ".join(braille_final))
        amount = int(input())
    if letter == "B":
        inp_inic = input().split()
        inp_meio = input().split()
        inp_final = input().split()
        resp = ""
        for x in range(0, amount):
            juncao = []
            juncao.append(inp_inic[x])
            juncao.append(inp_meio[x])
            juncao.append(inp_final[x])
            if juncao == braille[0]:
                resp += str(0)
            if juncao == braille[1]:
                resp += str(1)
            if juncao == braille[2]:
                resp += str(2)
            if juncao == braille[3]:
                resp += str(3)
            if juncao == braille[4]:
                resp += str(4)
            if juncao == braille[5]:
                resp += str(5)
            if juncao == braille[6]:
                resp += str(6)
            if juncao == braille[7]:
                resp += str(7)
            if juncao == braille[8]:
                resp += str(8)
            if juncao == braille[9]:
                resp += str(9)
        print(resp)
        amount = int(input())


