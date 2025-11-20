primeira = True

while True:
    nome = input()
    idade = int(input())

    if idade < 0:
        break

    if primeira:
        jovem_nome = velho_nome = nome
        jovem_idade = velho_idade = idade
        primeira = False
    else:
        if idade < jovem_idade:
            jovem_idade = idade
            jovem_nome = nome
        if idade > velho_idade:
            velho_idade = idade
            velho_nome = nome

print(jovem_nome)
print(jovem_idade)
print(velho_nome)
print(velho_idade)
