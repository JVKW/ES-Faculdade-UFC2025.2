nome_arquivo = input()

arquivo = open(nome_arquivo, 'r')

lista = []
for linha in arquivo:
    partes = linha.split('\t')
    nome = partes[0]
    telefone = partes[1].strip('\n')

    lista.append({
        'nome': nome,
        'telefone': telefone
    })

arquivo.close()

n = len(lista)
for i in range(n - 1):
    for j in range(i + 1, n):
        if lista[i]['nome'] > lista[j]['nome']:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

for item in lista:
    print(item)