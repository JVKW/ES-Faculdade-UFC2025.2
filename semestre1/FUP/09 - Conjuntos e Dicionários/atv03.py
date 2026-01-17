alunos = []

qtdAlunos = int(input())
for i in range(qtdAlunos):
    nome = input()
    matricula = int(input())
    curso = input()

    aluno = {
        'nome': nome,
        'matricula': matricula,
        'curso': curso
    }

    alunos.append(aluno)

for i in range(len(alunos)):
    print(alunos[i])