def simplificar(num, den):
    if num > den:
        maior = num
    elif num <= den:
        maior = den
    
    for i in range(maior, 1, -1):
        if num % i == 0:
            if den % i == 0:
                return num // i, den // i
    return num, den

x1 = int(input(""))
x2 = int(input(""))
y1, y2 = simplificar(x1, x2)
print(f"{y1}")
print(f"{y2}")