def gerar_triang(n):
    for i in range(1, n+1):
        print("*" * i)
    
    for i in range(n-1, 0, -1):
        print("*" * i)

    return

num = int(input("Digite o tamanho do Triângulo: "))

gerar_triang(num)