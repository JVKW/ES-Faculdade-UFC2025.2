def calc(n):
    sum = 0
    for n in range(1, n+1):
        sum += (n**2 + 1) / (n + 3)
    return sum

num = int(input("Digite o valor de N: "))

print(calc(num))