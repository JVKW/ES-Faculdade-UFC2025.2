def funcao(x, y):
    intersec = []
    for a in x:
        for b in y:
            if a == b:
                existe = False
                for c in intersec:
                    if c == a:
                        existe = True
                        break
                if not existe:
                    intersec.append(a)
                break
    return intersec

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)