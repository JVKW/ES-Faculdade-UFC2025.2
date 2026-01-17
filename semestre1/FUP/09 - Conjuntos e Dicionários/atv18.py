produtos = []
for _ in range(5):
    produtos.append({
        'codigo': int(input()),
        'nome': input(),
        'preco': float(input()),
        'quantidade': int(input())
    })

while True:
    for i in range(len(produtos)):
        print(produtos[i])

    codigo_pedido = int(input())

    if codigo_pedido == 0:
        break

    quantidade_pedido = int(input())

    encontrado = False

    for i in range(len(produtos)):
        produto = produtos[i]
        if produto['codigo'] == codigo_pedido:
            encontrado = True

            if produto['quantidade'] >= quantidade_pedido:
                produto['quantidade'] -= quantidade_pedido
            else:
                print('Impossivel atender ao pedido, produto sem estoque suficiente')
            break
    
    if not encontrado:
        print('Impossivel atender ao pedido, codigo nao encontrado')