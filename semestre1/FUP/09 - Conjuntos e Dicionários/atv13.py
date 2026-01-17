def verificarData(data):
    partes = data.split('/')

    if len(partes) != 3:
        return False

    for parte in partes:
        if parte == "":
            return False
        for c in parte:
            if c < '0' or c > '9':
                return False

    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    if mes < 1 or mes > 12:
        return False

    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia < 1 or dia > 30:
            return False
    else:
        if dia < 1 or dia > 31:
            return False

    return True

def verificarCep(cep):
    valido = True

    if len(cep) != 10:
        valido = False
    else:
        for i in range(10):
            if i == 2:
                if cep[i] != '.':
                    valido = False
            elif i == 6:
                if cep[i] != '-':
                    valido = False
            else:
                if cep[i] < '0' or cep[i] > '9':
                    valido = False
        
    return valido

def verificarEmail(email):
    dominios_validos = ["gmail", "yahoo", "hotmail"]

    tem_arroba = False
    pos_arroba = -1

    for i in range(len(email)):
        if email[i] == ' ':
            return False

        if email[i] == '@':
            if tem_arroba:
                return False
            tem_arroba = True
            pos_arroba = i

    if not tem_arroba:
        return False

    dominio = email[pos_arroba + 1:]
    dominio_ok = False

    for d in dominios_validos:
        if len(dominio) >= len(d):
            igual = True
            for i in range(len(d)):
                if dominio[i] != d[i]:
                    igual = False
            if igual:
                dominio_ok = True

    if not dominio_ok:
        return False

    tem_ponto = False
    for i in range(len(dominio)):
        if dominio[i] == '.':
            tem_ponto = True

    if not tem_ponto:
        return False

    if pos_arroba == 0 or pos_arroba == len(email) - 1:
        return False

    return True

def verificarInformacoes(usuario):
    if not verificarData(usuario['nascimento']):
        return 'Data errada'
    elif not verificarCep(usuario['cep']):
        return 'CEP errado'
    elif not verificarEmail(usuario['email']):
        return 'E-mail errado'
    else:
        return 0

nome = input()
endereco = input()
dataNascimento = input()
cidade = input()
cep = input()
email = input()

usuario = {
    'nome': nome,
    'endereco': endereco,
    'nascimento': dataNascimento,
    'cidade': cidade,
    'cep': cep,
    'email': email
}

verificao = verificarInformacoes(usuario)
if verificao == 0:
    print(usuario)
else:
    print(verificao)