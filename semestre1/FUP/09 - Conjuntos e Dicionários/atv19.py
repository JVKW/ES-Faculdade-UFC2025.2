pessoas = []

for i in range(5):
    pessoas.append({
        'nome': input('Nome: '),
        'endereco': {
            'rua': input('Rua: '),
            'bairro': input('Bairro: '),
            'cidade': input('Cidade: '),
            'estado': input('Estado: '),
            'cep': input('CEP: ')
        },
        'salario': float(input('Salario: ')),
        'identidade': input('Identidade: '),
        'cpf': input('CPF: '),
        'civil': input('Estado Civil: '),
        'telefone': input('Telefone: '),
        'idade': int(input('Idade: ')),
        'sexo': input('Sexo: ')
    })

maiorIdade = pessoas[0]
sexoMasculino = []
salarioAcimaDeMil = []

for i in range(len(pessoas)):
    pessoa = pessoas[i]

    if pessoa['idade'] > maiorIdade['idade']:
        maiorIdade = pessoa

    if pessoa['sexo'] == 'Masculino':
        sexoMasculino.append(pessoa)

    if pessoa['salario'] > 1000:
        salarioAcimaDeMil.append(pessoa)

print('Pessoa com maior idade:')
print(maiorIdade)

print('Pessoas do sexo masculino:')
for i in range(len(sexoMasculino)):
    print(sexoMasculino[i])

print('Pessoas com salario maior que 1000:')
for i in range(len(salarioAcimaDeMil)):
    print(salarioAcimaDeMil[i])

pesquisarIdentidade = input('Identidade: ')

for i in range(len(pessoas)):
    pessoa = pessoas[i]
    if pessoa['identidade'] == pesquisarIdentidade:
        print(pessoa)
        break
