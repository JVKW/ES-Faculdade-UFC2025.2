def funcao(vetor):
    n_rep = []
    for x in range(10):
        rep = False
        for y in range(10):
            if x != y and vetor[x] == vetor[y]:
                rep = True
                break
        if not rep:
            n_rep.append(vetor[x])

    return n_rep


x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)