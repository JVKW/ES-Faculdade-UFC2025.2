vetor = []

cont = 0
while cont < 12:
    entrada = int(input())

    existe = False
    for v in vetor:
        if v == entrada:
            existe = True
            break
    if existe:
        print(f"Numero {entrada} ja existe, escreva outro")
        continue
    else:
        vetor.append(entrada)
        cont += 1

print(vetor)