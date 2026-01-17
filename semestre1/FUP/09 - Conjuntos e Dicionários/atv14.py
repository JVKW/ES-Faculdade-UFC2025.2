carros = []

for i in range(5):
    marca = input()
    ano = int(input())
    preco = float(input())

    carros.append({
        'modelo': marca,
        'ano': ano,
        'preco': preco
    })

while True:
    p = float(input())
    if p == 0:
        break

    for i in range(len(carros)):
        if carros[i]['preco'] < p:
            print(carros[i])
