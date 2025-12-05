def fat(x):
    tot = 1
    for i in range(2, x + 1):
        tot *= i
    return tot

def sf(n):
    if n == 0:
        return 1
    else:
        return fat(n) * sf(n - 1)