def soma(z, w):
    return {
        'real': z['real'] + w['real'],
        'imaginario': z['imaginario'] + w['imaginario']
    }

def subtracao(z, w):
    return {
        'real': z['real'] - w['real'],
        'imaginario': z['imaginario'] - w['imaginario']
    }

def produto(z, w):
    return {
        'real': z['real'] * w['real'] - z['imaginario'] * w['imaginario'],
        'imaginario': z['real'] * w['imaginario'] + z['imaginario'] * w['real']
    }

def modulo(z):
    return (z['real'] ** 2 + z['imaginario'] ** 2) ** 0.5

z = {
    'real': float(input()),
    'imaginario': float(input())
}

w = {
    'real': float(input()),
    'imaginario': float(input())
}

print(soma(z, w))
print(subtracao(z, w))
print(produto(z, w))
print(f"{modulo(z):.2f}")
print(f"{modulo(w):.2f}")