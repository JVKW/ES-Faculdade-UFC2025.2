def trocar_0(p):
    str_result = ''
    for i in str(p):
        if i == '0':
            str_result += '1'
        else:
            str_result += i
    
    return str_result

p1 = str(input())
print(trocar_0(p1))