soma = 0
cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} numeros impares multiplos de 3 entre 1 e 500 é: {soma}')
