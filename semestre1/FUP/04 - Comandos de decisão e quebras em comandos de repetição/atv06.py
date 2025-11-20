soma = 0
i = 0
while i < 3:
    nota = float(input(f"Digite a nota {i + 1}: "))
    if nota < 0:
        print("Nota inválida")
        break
    elif nota > 10:
        print("Nota inválida")
        break
    else:
        soma += nota
        i += 1
        if i == 3:
            print(f"A média da nota é: {soma/3}")