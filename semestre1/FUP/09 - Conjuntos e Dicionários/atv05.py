def calcularMedia(alunoDic):
    soma = 0
    nNotas = len(alunoDic['notas'])
    for i in range(nNotas):
        soma += alunoDic['notas'][i]
    return soma / nNotas


def pegarMaiorPrimeiraNota(alunos):
    iMaior = 0
    for i in range(len(alunos)):
        if alunos[i]['notas'][0] > alunos[iMaior]['notas'][0]:
            iMaior = i
    return alunos[iMaior]


def pegarMaiorMenorMedia(alunos):
    maiorMedia = calcularMedia(alunos[0])
    menorMedia = maiorMedia
    iMaior = 0
    iMenor = 0

    for i in range(len(alunos)):
        media = calcularMedia(alunos[i])
        if media > maiorMedia:
            maiorMedia = media
            iMaior = i
        if media < menorMedia:
            menorMedia = media
            iMenor = i

    return alunos[iMaior], alunos[iMenor]

alunos = []

for i in range(5):
    matricula = int(input())
    nome = input()
    notas = []

    for j in range(3):
        notas.append(float(input()))

    aluno = {
        'matricula': matricula,
        'nome': nome,
        'notas': notas
    }

    alunos.append(aluno)

alunoMaiorNota1 = pegarMaiorPrimeiraNota(alunos)
print(f"Aluno {alunoMaiorNota1['nome']} tem a maior nota1: {alunoMaiorNota1['notas'][0]:.2f}")

alunoMaiorMedia, alunoMenorMedia = pegarMaiorMenorMedia(alunos)

print(f"Aluno {alunoMaiorMedia['nome']} tem a maior media: {calcularMedia(alunoMaiorMedia):.2f}")
print(f"Aluno {alunoMenorMedia['nome']} tem a menor media: {calcularMedia(alunoMenorMedia):.2f}")

for i in range(len(alunos)):
    media = calcularMedia(alunos[i])
    if media >= 7:
        print(f"Aluno {alunos[i]['nome']} esta aprovado com media {media:.2f}")
    else:
        print(f"Aluno {alunos[i]['nome']} esta reprovado com media {media:.2f}")
