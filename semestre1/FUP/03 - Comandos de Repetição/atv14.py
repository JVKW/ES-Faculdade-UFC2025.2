def serie_harm(x):
    Hn = 0
    for i in range(1, x+1):
        Hn += 1/i

    return Hn

num = int(input("Digite o valor de n: "))

print(f"Série Harmônica H({num}) = {serie_harm(num):.2f}")