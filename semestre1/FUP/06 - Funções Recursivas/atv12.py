def h(m, n):
    if n == 1:
        return m + 1
    elif m == 1:
        return n + 1
    elif m > 1 and n > 1:
        return h(m, n-1) + h(m-1, n)
    
x1 = int(input(""))
x2 = int(input(""))
y = h(x1, x2)
print(f"{y}")