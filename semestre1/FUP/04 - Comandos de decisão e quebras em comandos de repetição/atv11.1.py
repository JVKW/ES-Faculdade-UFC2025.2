num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada: ")
num2 = float(input("Digite o segundo número: "))

match operacao:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)