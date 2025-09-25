from math import pi

def cal_esfera(raio):
    volume = (4 * pi * raio ** 3)/3
    area = (4 * pi * raio ** 2)

    return volume, area

volume, area = cal_esfera(5)

print(f"Volume da Esfera: {volume} cm³\nÁrea da Esfera: {area} cm²")