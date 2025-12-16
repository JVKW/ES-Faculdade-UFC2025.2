def funcao(vetor, x):
    mult = []
    for i in vetor:
        if i % x == 0:
            mult.append(i)
    
    return mult

x1 = []
for i in range(10):
    x1.append(int(input("")))
x2 = int(input(""))
y = funcao(x1, x2)
print(y)