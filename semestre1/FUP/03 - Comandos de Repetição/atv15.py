def cal_fatorial(x):
        prod = 1
        for i in range(x):
            prod *= i + 1
        
        return prod

def cal_E(n):
    cE = 1
    for i in range(1, n+1):
        cE += 1/cal_fatorial(i)

    return cE

num = int(input("Digite o valor de n: "))

print(f"Calcular E({num}) = {cal_E(num):.5f}")