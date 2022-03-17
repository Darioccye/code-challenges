fn = input()
qn = fn.split()

n1 = float(qn[0])
n2 = float(qn[1])
n3 = float(qn[2])
n4 = float(qn[3])

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10

if media >= 7:
    message_aprv = """Media: %s
Aluno aprovado.""" % format(media, ".1f")
    print(message_aprv)
elif media < 5:
    message_n_aprv = """Media: %s
Aluno reprovado.""" % format(media, ".1f")
    print(message_n_aprv)
else:
    sn = float(input())
    media_rec = (media + sn) / 2
    if media_rec >= 5:
        message_exam_aprv = """Media: %s
Aluno em exame.
Nota do exame: %s
Aluno aprovado.
Media final: %s""" % (format(media, ".1f"),  format(sn, ".1f"), format(media_rec, ".1f"))
        print(message_exam_aprv)
    if media_rec < 5:
        message_exam_n_aprv = """Media: %s
Aluno em exame.
Nota do exame: %s
Aluno reprovado.
Media final: %s""" % (format(media, ".1f"),  format(sn, ".1f"), format(media_rec, ".1f"))
        print(message_exam_n_aprv)





