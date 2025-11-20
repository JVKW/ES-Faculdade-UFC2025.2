for i in range(1000, 10000):
    calc = (i // 100) + (i % 100)
    if calc ** 2 == i:
        print(i)