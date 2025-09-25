def separar_num(num):
    mil = num // 1000
    cen = (num // 100) % 10
    dez = (num // 10) % 10
    uni = num % 10
    
    return mil, cen, dez, uni

print(separar_num(9274))
