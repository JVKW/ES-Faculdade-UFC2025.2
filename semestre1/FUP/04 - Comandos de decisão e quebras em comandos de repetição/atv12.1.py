escolha = int(input("Digite o valor da tabela(1-4): "))

match escolha:
    case 1:
        print("Bom Dia - Boa Tarde - Boa Noite")
    case 2:
        print("Por favor :) - Com Licença :D - Muito Obrigado ;)")
    case 3:
        print("Por Gentileza - Você poderia - Desculpe")
    case 4:
        print("Boa Sorte - Tenha Fe")
    case _:
        print("Estudar vale muito a pena!")