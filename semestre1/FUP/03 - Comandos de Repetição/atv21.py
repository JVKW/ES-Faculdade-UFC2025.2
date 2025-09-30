def gerar_triang(n):
    for i in range(1, n+1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

num = int(input("Digite o tamanho do Triângulo: "))

gerar_triang(num)

# 5 -----*
# 4 ----***
# 3 ---*****
# 2 --*******
# 1 -*********
# 0 ***********