def SomaSerie(i, j, k):
    if i > j:
        return 0
    else:
        return i + SomaSerie(i + k, j, k)

x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
y = SomaSerie(x1, x2, x3)
print(f"{y}")