num = int(input())

div3 = (num % 3 == 0)
div5 = (num % 5 == 0)

if div3 != div5:
    print(True)
else:
    print(False)
