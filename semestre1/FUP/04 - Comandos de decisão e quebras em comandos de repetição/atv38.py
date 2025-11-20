def funcao(str1, str2):
    if len(str1) > len(str2):
        return False
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

x1 = input("")
x2 = input("")
y = funcao(x1, x2)
print(f"{y}")