def funcao(a, b):
    if a > b:
        m = a
    else:
        m = b

    while True:
        if m % a == 0 and m % b == 0:
            return m
        m += 1