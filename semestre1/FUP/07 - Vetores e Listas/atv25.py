def funcao(x, y):
    uni = []

    for a in x:
        existe = False
        for u in uni:
            if a == u:
                existe = True
                break
        if not existe:
            uni.append(a)
    
    for b in y:
        existe = False
        for u in uni:
            if b == u:
                existe = True
                break
        if not existe:
            uni.append(b)
        
    return uni

x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)