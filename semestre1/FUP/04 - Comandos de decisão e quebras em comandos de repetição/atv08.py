num1 = float(input("Digite o número 1: "))
num2 = float(input("Digite o número 2: "))
escolha = int(input("Digite sua escolha (1-4): "))

if escolha == 1:
    print("Média:", (num1 + num2) / 2)

elif escolha == 2:
    if num1 > num2:
        print("Diferença do maior pelo menor:", num1 - num2)
    else:
        print("Diferença do maior pelo menor:", num2 - num1)

elif escolha == 3:
    print("Produto:", num1 * num2)

elif escolha == 4:
    if num2 != 0:
        print("Divisão do primeiro pelo segundo:", num1 / num2)
    else:
        print("O segundo número deve ser diferente de 0")

else:
    print("Opção inválida!")
