livros = []
for i in range(5):
    titulo = input()
    autor = input()
    ano = int(input())

    livros.append({
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    })

busca = input()

resultadoPesquisa = []
for livro in range(len(livros)):
    titulo = livros[livro]['titulo']
    encontrado = False

    for i in range(len(titulo) - len(busca) + 1):
        igual = True
        for j in range(len(busca)):
            if titulo[i + j].lower() != busca[j].lower():
                igual = False

        if igual:
            encontrado = True
            break

    if encontrado:
        resultadoPesquisa.append(livros[livro])

for i in range(len(resultadoPesquisa)):
    print(resultadoPesquisa[i])