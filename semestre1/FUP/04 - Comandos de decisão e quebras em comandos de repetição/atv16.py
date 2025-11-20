primeiro = 1

while True:
    num = int(input())
    if num < 0:
        break

    if primeiro == 1:
        maior = menor = num
        primeiro = 0
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

if primeiro == 0:
    print(maior)
    print(menor)
