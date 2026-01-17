def maisEconomico(lista):
    nomeMaisEconomico = ''

    maiorEconomia = 0
    for i in range(len(lista)):
        consumoCarro = lista[i]['consumo']
        if consumoCarro > maiorEconomia:
            maiorEconomia = consumoCarro
            nomeMaisEconomico = lista[i]['nome']
    
    return nomeMaisEconomico

def calcularQuilometragem(consumo, litros):
    return consumo * litros

def calcularCombustivel(quilometros, consumo):
    return quilometros / consumo

carros = []

for i in range(5):
    nome = input()
    consumo = float(input())
    car = {
        'nome': nome,
        'consumo': consumo
    }
    carros.append(car)

carroMaisEconomico = maisEconomico(carros)
print(f"Carro mais economico: {carroMaisEconomico}")

tam_list = len(carros)
for i in range(tam_list):
    carro = carros[i]
    print(f"Carro {carro['nome']} percorre {calcularQuilometragem(carro['consumo'], 50):.2f} kms com 50 litros")

for i in range(tam_list):
    carro = carros[i]
    print(f"Carro {carro['nome']} precisa de {calcularCombustivel(1000, carro['consumo']):.2f} litros para percorrer 1000 kms")