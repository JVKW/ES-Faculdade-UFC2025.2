pares = []

for i in range(15):
    val = int(input())
    if val % 2 == 0:
        pares.append(val)

print(len(pares))

for i in pares:
    print(i)