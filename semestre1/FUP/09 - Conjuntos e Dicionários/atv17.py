def calcular_consumo(potencia_kw, tempo_h):
    return potencia_kw * tempo_h

def calcular_consumo_geral(aparelhos, dias):
    consumo_total = 0
    consumos = []

    for i in range(len(aparelhos)):
        aparelho = aparelhos[i]
        consumo = calcular_consumo(aparelho['potencia'], aparelho['tempo']) * dias
        consumo_total += consumo

        consumos.append({
            'nome': aparelho['nome'],
            'consumo': consumo
        })

    for i in range(len(consumos)):
        consumos[i]['porcentagem'] = (consumos[i]['consumo'] / consumo_total) * 100

    return consumo_total, consumos

eletrodomesticos = []
for i in range(5):
    eletrodomesticos.append({
        'nome': input(),
        'potencia': float(input()),
        'tempo': float(input())
    })

dias = int(input())

consumo_total, consumos = calcular_consumo_geral(eletrodomesticos, dias)

print(f"{consumo_total:.2f}")
for i in range(len(consumos)):
    print(f"{consumos[i]['nome']}: {consumos[i]['porcentagem']:.2f}")
