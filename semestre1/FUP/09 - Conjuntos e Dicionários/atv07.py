tamanhoTurma = int(input())

def calcularMediaPonderada(notas):
    somaNotas = 0
    somaPesos = 0
    tam = len(notas)

    for i in range(tam):
        notaDic = notas[i]
        nota = notaDic['nota']
        peso = notaDic['peso']
        somaNotas += nota * peso
        somaPesos += peso
    
    return somaNotas / somaPesos

alunos = []
for i in range(tamanhoTurma):
    matricula = int(input())
    nome = input()
    codigoDisciplina = input()
    nota1 = float(input())
    nota2 = float(input())
    media = calcularMediaPonderada(
        [
            {'nota': nota1, 'peso': 1},
            {'nota': nota2, 'peso': 2}
        ]
    )

    alunos.append({
        'matricula': matricula,
        'nome': nome,
        'codigo': codigoDisciplina,
        'nota1': nota1,
        'nota2': nota2,
        'media': media
    })

for i in range(len(alunos)):
    print(alunos[i])