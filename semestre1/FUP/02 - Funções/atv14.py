def inverter_num(num):
    cen = num // 100
    dez = (num // 10) % 10
    uni = num % 10
    
    return uni * 100 + dez * 10 + cen

print(inverter_num(942))
