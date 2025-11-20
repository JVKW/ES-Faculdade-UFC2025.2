while True:
    print("1 - Adicao")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Saida")
    
    opcao = int(input())
    
    if opcao == 5:
        break
    
    num1 = float(input())
    num2 = float(input())
    
    if opcao == 1:
        print(f"{num1 + num2:.2f}")
    elif opcao == 2:
        print(f"{num1 - num2:.2f}")
    elif opcao == 3:
        print(f"{num1 * num2:.2f}")
    elif opcao == 4:
        if num2 != 0:
            print(f"{num1 / num2:.2f}")
        else:
            print("Erro: divisão por zero.")
    else:
        print("Opção inválida.")
