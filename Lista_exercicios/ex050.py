soma = 0
cont = 0
for c in range(0, 6, 1):
    n = int(input(f'Digite {c}º número: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} numeros pares digitados é: {soma}')
