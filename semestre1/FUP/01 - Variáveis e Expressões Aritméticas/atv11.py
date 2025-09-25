salario = float(input("Salário: R$ "))
aumento = 21.37

salario_aum = salario + salario * (aumento/100)

print(f"Salário: R${salario} - Aumento de {aumento}%: R${salario_aum}")