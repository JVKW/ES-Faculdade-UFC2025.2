impares = []
soma = 0

for i in range(15):
    val = int(input())
    if val % 2 != 0:
        impares.append(val)
        soma += val

print(soma)

for i in impares:
    print(i)
