frase = input()

frase_inv = ''

i = len(frase) - 1
while i >= 0:
    carac = frase[i]
    
    if carac == 'A':
        frase_inv += '*'
    elif carac == 'a':
        frase_inv += '*'
    else:
        frase_inv += carac
        
    i -= 1

print(frase_inv)