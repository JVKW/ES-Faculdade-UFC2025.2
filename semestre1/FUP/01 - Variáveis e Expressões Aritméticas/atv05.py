from math import pi

raio = float(input("Raio da Esfera: (cm)"))

volume = (4 * (raio ** 3) * pi)/3

area = 4 * pi * raio ** 2

print(f"Volume Esfera: {volume:.2f}cm³")
print(f"Area Esfera: {area:.2f}cm²")