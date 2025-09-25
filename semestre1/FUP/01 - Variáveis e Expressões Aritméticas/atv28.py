string1 = input("Digite uma string: ")
string2 = input("Digite outra string: ")

resultado = string1[-len(string2):] == string2

print(f"'{string2}' está contida no final de '{string1}': {resultado}")