def cal_fatorial(x):
    produto = 1
    for i in range(x):
        produto *= i + 1
    
    return produto

num = int(input("Digite o número: "))
print(f"{num}! = {cal_fatorial(num)}")
