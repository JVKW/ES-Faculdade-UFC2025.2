def coeficiente_binominal(n, k):
    def cal_fatorial(x):
        prod = 1
        for i in range(int(x)):
            prod *= i + 1
        
        return prod
    
    fat_n = cal_fatorial(n)
    fat_k = cal_fatorial(k)
    fat_kn = cal_fatorial(n-k)

    return fat_n/(fat_k*(fat_kn))

valn = float(input("Digite o valor de n: "))
valk = float(input("Digite o valor de k: "))

print(f"O valor do Coeficiente Binominal C(n,k) = n!/(k!*(n-k)!) => {coeficiente_binominal(valn, valk)}")