def verificar_nota(n1, n2, n3, tipo):
    if tipo == 'A':
        return float(f'{(n1 + n2 + n3)/3:.2f}')
    elif tipo == 'P':
        return float(f'{(n1*5 + n2*3 + n3*2)/10:.2f}')
    
print(verificar_nota(10, 9.5, 3, 'A'))