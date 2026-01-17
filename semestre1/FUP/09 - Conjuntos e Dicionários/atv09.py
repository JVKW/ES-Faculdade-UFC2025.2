nome = input()
idade = int(input())
sexo = input()
cpf = input()
dataNascimento = input()
codigoSetor = int(input())
cargo = input()
salario = float(input())

funcionario = {
    'nome': nome,
    'idade': idade,
    'sexo': sexo,
    'cpf': cpf,
    'nascimento': dataNascimento,
    'setor': codigoSetor,
    'cargo': cargo,
    'salario': salario
}

print(funcionario)