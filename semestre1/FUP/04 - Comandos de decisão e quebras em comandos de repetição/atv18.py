def data_extenso(data):
    dia = data[:2]
    mes_num = int(data[3:5])
    ano = data[6:]
    
    if mes_num == 1:
        mes = 'janeiro'
    if mes_num == 2:
        mes = 'fevereiro'
    if mes_num == 3:
        mes = 'março'
    if mes_num == 4:
        mes = 'abril'
    if mes_num == 5:
        mes = 'maio'
    if mes_num == 6:
        mes = 'junho'
    if mes_num == 7:
        mes = 'julho'
    if mes_num == 8:
        mes = 'agosto'
    if mes_num == 9:
        mes = 'setembro'
    if mes_num == 10:
        mes = 'outubro'
    if mes_num == 11:
        mes = 'novembro'
    if mes_num == 12:
        mes = 'dezembro'
    
    return f'{int(dia)} de {mes} de {ano}'

x = input("Digite uma data em formato: [DD/MM/AA]: ")
y = data_extenso(x)
print(f"{y}")