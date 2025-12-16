alunos = []

i = 0
while i < 5:
    aluno = input("Aluno: ")
    alunos.append(aluno)

    if i != 4:
        res = input("Deseja inserir novo aluno? [S/N] ").upper()
        if res == "N":
            break

    i += 1

search = input("Aluno para pesquisa: ")

result = []
for i in range(len(alunos)):
    if alunos[i].find(search) != -1:
        print(alunos[i])
        print(i)

print(result)