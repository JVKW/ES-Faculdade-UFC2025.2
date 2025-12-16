def funcao(notas):
    soma = 0
    AF = 0
    for i in notas:
        soma += i
        if i < 7:
            AF += 1
    media = soma / len(notas)

    somatorio = 0
    for i in notas:
        somatorio += (i - media)**2
    desvio = (somatorio / len(notas))**0.5

    return media, desvio, AF

x = []
for i in range(15):
    x.append(float(input("")))
y1, y2, y3 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3}")