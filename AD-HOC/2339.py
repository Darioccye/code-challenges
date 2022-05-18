alunos, papeis, papeis_por_aluno = map(int, input().split())

if alunos*papeis_por_aluno <= papeis:
    print("S")
else:
    print("N")
