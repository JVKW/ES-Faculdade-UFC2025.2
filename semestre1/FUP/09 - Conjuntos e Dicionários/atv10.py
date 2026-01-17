pessoas = []

def ordenarAlfabeticamente(pessoas):
    n = len(pessoas)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if pessoas[j]['nome'].lower() > pessoas[j + 1]['nome'].lower():
                aux = pessoas[j]
                pessoas[j] = pessoas[j + 1]
                pessoas[j + 1] = aux

for i in range(5):
    nome = input()
    endereco = input()
    telefone = input()

    pessoas.append({
        'nome': nome,
        'endereco': endereco,
        'telefone': telefone
    })

ordenarAlfabeticamente(pessoas)

for i in range(len(pessoas)):
    print(pessoas[i])
