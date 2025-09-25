x = float(input("Coordenada X: "))
y = float(input("Coordenada Y: "))

ori_x = 0
ori_y = 0

distancia = ((ori_x - x)**2 + (ori_y - y)**2)**0.5

print(f"Distância de A({ori_x},{ori_y}) até B({x},{y}): {distancia:.2f}")