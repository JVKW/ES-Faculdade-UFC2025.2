agenda = []

def inserirPessoa():
    pessoa = {
        'nome': input('Nome: '),
        'email': input('E-mail: '),
        'endereco': {
            'rua': input('Rua: '),
            'numero': int(input('Numero: ')),
            'complemento': input('Complemento: '),
            'bairro': input('Bairro: '),
            'cep': input('CEP: '),
            'cidade': input('Cidade: '),
            'estado': input('Estado: '),
            'pais': input('Pais: ')
        },
        'telefone': {
            'ddd': int(input('DDD: ')),
            'numero': input('Telefone: ')
        },
        'nascimento': {
            'dia': int(input('Dia do nascimento: ')),
            'mes': int(input('Mes do nascimento: ')),
            'ano': int(input('Ano do nascimento: '))
        },
        'observacao': input('Observacao: ')
    }
    agenda.append(pessoa)

def buscarPrimeiroNome(nome_busca):
    encontrados = []
    for pessoa in agenda:
        primeiro_nome = ""
        for letra in pessoa['nome']:
            if letra == ' ':
                break
            primeiro_nome += letra
        
        encontrado = True
        if len(nome_busca) <= len(primeiro_nome):
            for i in range(len(nome_busca)):
                if primeiro_nome[i].lower() != nome_busca[i].lower():
                    encontrado = False
                    break
            if encontrado:
                encontrados.append(pessoa)
    return encontrados

def buscarAniversarioPorMes(mes_busca):
    encontrados = []
    for pessoa in agenda:
        if pessoa['nascimento']['mes'] == mes_busca:
            encontrados.append(pessoa)
    return encontrados

def buscarAniversarioPorMesEDia(mes_busca, dia_busca):
    encontrados = []
    for pessoa in agenda:
        if pessoa['nascimento']['mes'] == mes_busca and pessoa['nascimento']['dia'] == dia_busca:
            encontrados.append(pessoa)
    return encontrados

def imprimirResumo(pessoa):
    print({'nome': pessoa['nome'], 'telefone': pessoa['telefone'], 'email': pessoa['email']})


def imprimirCompleto(pessoa):
    print(pessoa)

def imprimirLista(lista, completa):
    for pessoa in lista:
        if completa:
            print(pessoa)
        else:
            print({'nome': pessoa['nome'], 'telefone': pessoa['telefone'], 'email': pessoa['email']})

def imprimirAgenda():
    print('1: Imprimir apenas nome, telefone e email')
    print('2: Imprimir todos os dados')
    opcao = int(input('Opcao: '))
    if opcao == 1:
        imprimirLista(agenda, False)
    elif opcao == 2:
        imprimirLista(agenda, True)
    else:
        print('Opcao invalida')

def menu():
    while True:
        print('1: Inserir uma pessoa')
        print('2: Buscar por primeiro nome')
        print('3: Buscar por mes de nascimento')
        print('4: Buscar por dia e mes de nascimento')
        print('5: Imprimir agenda')
        print('0: Sair')
        opcao = int(input('Opcao: '))
        
        if opcao == 1:
            inserirPessoa()
        elif opcao == 2:
            nome = input('Primeiro nome: ')
            resultado = buscarPrimeiroNome(nome)
            for pessoa in resultado:
                print(pessoa)
        elif opcao == 3:
            mes = int(input('Mes de nascimento: '))
            resultado = buscarAniversarioPorMes(mes)
            imprimirLista(resultado, True)
        elif opcao == 4:
            dia = int(input('Dia do nascimento: '))
            mes = int(input('Mes do nascimento: '))
            resultado = buscarAniversarioPorMesEDia(mes, dia)
            imprimirLista(resultado, True)
        elif opcao == 5:
            imprimirAgenda()
        elif opcao == 0:
            break
        else:
            print('Opcao invalida')

menu()