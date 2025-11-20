salario = float(input("Digite o valor do salário: "))
emprestimo = float(input("Digite o valor do Empréstimo: "))

if emprestimo > (salario * 0.2):
    print("Empréstimo Não Concedido.")
else:
    print("Empréstimo Concedido")