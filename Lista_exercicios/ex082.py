geral = list()
pares = list()
impares = list()
while True:
    resp = ' '
    geral.append(int(input('Digite um valor: ')))
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [ S / N ]')).strip().upper()[0]
    if resp == 'N':
        break
for num in geral:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'A lista completa é: {geral}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')
