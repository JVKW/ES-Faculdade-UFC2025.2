def fatorial(x):
    fat = 1
    for i in range(1, x+1):
        fat *= i
    return fat

def cal_fat_exp(n):
    total = 1
    for i in range(2, n+1):
        total = i ** total

# n = 5 => 5 ** (4 ** (3 ** (2 ** (1))))

print(cal_fat_exp(3)) # n | n >= 5 é necessário configuração