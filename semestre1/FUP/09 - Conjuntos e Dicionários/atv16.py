def ordenarCompromissos(compromissos):
    n = len(compromissos)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            data1 = compromissos[j]['data']
            data2 = compromissos[j + 1]['data']

            trocar = False

            if data1['ano'] > data2['ano']:
                trocar = True
            elif data1['ano'] == data2['ano']:
                if data1['mes'] > data2['mes']:
                    trocar = True
                elif data1['mes'] == data2['mes']:
                    if data1['dia'] > data2['dia']:
                        trocar = True

            if trocar:
                aux = compromissos[j]
                compromissos[j] = compromissos[j + 1]
                compromissos[j + 1] = aux

    return compromissos

agenda = []

for i in range(5):
    compromisso = input("Descricao: ")
    data = {
        'dia': int(input('Dia: ')),
        'mes': int(input('Mes: ')),
        'ano': int(input('Ano: '))
    }

    agenda.append({
        'compromisso': compromisso,
        'data': data
    })

while True:
    M = int(input())
    if M == 0:
        break
    A = int(input())


    existentes = []
    for i in range(len(agenda)):
        compromisso = agenda[i]
        if compromisso['data']['ano'] == A and compromisso['data']['mes'] == M:
            existentes.append(compromisso)

    existentes = ordenarCompromissos(existentes)

    for i in range(len(existentes)):
        print(existentes[i])