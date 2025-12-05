def funcao(x):
    if x == 1 or x <= 0:
        return 1
    else:
        return x * funcao(x - 1)