def retangulo(base, largura):
    area = base * largura
    perimetro = (base + largura) * 2
    return area, perimetro

area, perimetro = retangulo(base=5, largura=3)

print(f"Perímetro do Retângulo: {perimetro} cm")
print(f"Área do Retângulo: {area} cm")