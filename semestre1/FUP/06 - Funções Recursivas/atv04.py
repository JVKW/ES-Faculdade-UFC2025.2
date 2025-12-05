def funcao(n, k):
    if k == 0:
        return 1
    else:
        return n * funcao(n, k-1)