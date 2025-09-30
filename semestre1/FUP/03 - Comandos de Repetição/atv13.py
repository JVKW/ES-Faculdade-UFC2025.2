def fibonacci(n):
    f1 = 1
    f2 = 1

    for _ in range(n-1):
        af = f1
        f1 = f2
        f2 = af + f2

    return f1

n = int(input("Digite n: "))
print(f"F(n) = {fibonacci(n)}")