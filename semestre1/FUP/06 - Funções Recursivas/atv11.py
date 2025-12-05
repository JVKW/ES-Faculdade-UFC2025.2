def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x%y)

x1 = int(input(""))
x2 = int(input(""))
y = mdc(x1, x2)
print(f"{y}")