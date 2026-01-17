alunos = []
for i in range(10):
    nome = input()
    matricula = int(input())
    media = float(input())

    alunos.append({
        'nome': nome,
        'matricula': matricula,
        'media': media
    })

aprovados = []
reprovados = []
for i in range(len(alunos)):
    aluno = alunos[i]
    if aluno['media'] >= 5:
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

for i in range(len(aprovados)):
    print(aprovados[i])
for i in range(len(reprovados)):
    print(reprovados[i])