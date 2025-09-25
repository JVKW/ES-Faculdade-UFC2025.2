def cal_adjacentes(num: int):
    return num - 1, num + 1

antecessor, sucessor = cal_adjacentes(5)

print("Antecessor:", antecessor)
print("Sucessor:", sucessor)