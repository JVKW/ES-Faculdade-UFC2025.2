n1 = int(input())
n2 = int(input())

def cal_intervalo(maior, menor):
    soma_pares = 0
    mult_impar = 1
    
    for i in range(menor, maior+1):
        if i % 2 == 0:
            soma_pares += i
        else:
            mult_impar *= i
    return soma_pares, mult_impar

if n1 >= n2:
    maior = n1
    menor = n2
elif n2 > n1:
    maior = n2
    menor = n1
    
soma_pares, mult_impar = cal_intervalo(maior, menor)

print(soma_pares)
print(mult_impar)