def criarDicCompromisso():
    dia = int(input())
    mes = int(input())
    ano = int(input())

    hora = int(input())
    minuto = int(input())
    segundo = int(input())

    descricao = input()

    data = {
        'dia': dia,
        'mes': mes,
        'ano': ano
    }

    horario = {
        'hora': hora,
        'minuto': minuto,
        'segundo': segundo
    }

    return {
        'data': data,
        'horario': horario,
        'descricao': descricao
    }

def calcularChaveDataHora(compromisso):
    data = compromisso['data']
    horario = compromisso['horario']

    return (
        data['ano'] * 10000000000 +
        data['mes'] * 100000000 +
        data['dia'] * 1000000 +
        horario['hora'] * 10000 +
        horario['minuto'] * 100 +
        horario['segundo']
    )

def compromisso_antes(c1, c2):
    chave1 = calcularChaveDataHora(c1)
    chave2 = calcularChaveDataHora(c2)

    if chave1 < chave2:
        return True
    else:
        return False

def ordenarCompromissos(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not compromisso_antes(lista[j], lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista

compromissos = []

nCompromissos = int(input())
for i in range(nCompromissos):
    compromissos.append(criarDicCompromisso())

listaCompromissosOrdenados = ordenarCompromissos(compromissos)

print(nCompromissos)

for i in range(len(listaCompromissosOrdenados)):
    c = listaCompromissosOrdenados[i]
    d = c['data']
    h = c['horario']

    print("Dia:", d['dia'])
    print("Mes:", d['mes'])
    print("Ano:", d['ano'])
    print("Hora:", f"{h['hora']:02d}")
    print("Minuto:", f"{h['minuto']:02d}")
    print("Segundo:", f"{h['segundo']:02d}")
    print("Descricao:", c['descricao'])

for i in range(nCompromissos):
    print(listaCompromissosOrdenados[i])