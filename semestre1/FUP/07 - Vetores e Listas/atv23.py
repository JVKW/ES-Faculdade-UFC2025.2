vetor = []

for i in range(10):
    val = int(input())
    vetor.append(val)

cont = 0
for i in vetor:

    n = abs(i)

    if n < 2:
        cont += 1
        continue

    primo = True

    for y in range(2, int(n ** 0.5) + 1):
        if n % y == 0:
            primo = False
            break

    if primo:
        print(i)
        print(cont)
    cont += 1