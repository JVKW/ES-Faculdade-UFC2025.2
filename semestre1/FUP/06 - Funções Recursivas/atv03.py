def funcao(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return x**3 + funcao(x - 1)
