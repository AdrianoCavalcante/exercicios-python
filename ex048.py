s = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        s += c
print(f'A soma dos numeros impares multiplos de 3 entre 1 e 500 é: {s}')
