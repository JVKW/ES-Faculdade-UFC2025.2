def val_quad(x, n):
    resultado = 1
    for _ in range(n):
        resultado *= x
    return resultado


x = int(input("Digite x: "))
y = int(input("Digite y: "))

print(f"{x}^{y} = {val_quad(x, y)}")
