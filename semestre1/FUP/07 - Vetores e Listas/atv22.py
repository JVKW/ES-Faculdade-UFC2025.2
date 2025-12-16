vetor = []

cont = 0
while True:
    if cont % 7 != 0 and cont % 10 != 7:
        vetor.append(cont)
    if len(vetor) == 100:
        break
    cont += 1

print(vetor)