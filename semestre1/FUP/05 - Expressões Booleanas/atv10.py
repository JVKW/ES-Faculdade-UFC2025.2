def funcao(a, b):
    if a < b:
        m = a
    else:
        m = b

    while m > 0:
        if a % m == 0 and b % m == 0:
            return m
        m -= 1