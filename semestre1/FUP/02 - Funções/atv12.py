def cal_aumento(salario):
    aumento = 21.37
    return salario + salario * (aumento/100)

novo_salario = cal_aumento(1000)

print(f"Salário: R${novo_salario}")