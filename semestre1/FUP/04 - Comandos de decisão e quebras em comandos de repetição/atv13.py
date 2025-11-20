a = 5
b = 2
c = -15

if a == 0:
    print("Não é equação do 2º Grau.")
else:
    delta = b ** 2 - (4 * a * c)

    if delta < 0:
        print("Não existe raiz real.")
    elif delta == 0:
        print(f"Raiz única: {-b / (2 * a)}")
    elif delta > 0:
        x1 = (-b + delta ** 0.5)/(2 * a)
        x2 = (-b - delta ** 0.5)/(2 * a)

        print(f"Raiz x1: {x1}")
        print(f"Raiz x2: {x2}")