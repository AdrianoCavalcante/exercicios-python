num = numsoma = cont = menor = maior = 0
resp = ''
while resp != 'N':
    num = int(input('Didite um numero: '))
    cont += 1
    numsoma += num
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja incluir mais um numero? [ S ] ou [ N ]: ')).strip().upper()[0]
    if resp not in ['S', 'N']:
        while resp not in ['S', 'N']:
            print('NÃO ENTENDI FAVOR DIGITAR APENAS "S" PARA SIM E "N" PARA NÃO!')
            resp = str(input('Deseja incluir mais um numero? [ S ] ou [ N ]: ')).strip().upper()[0]
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Entradas: {cont}')
print(f'Soma: {numsoma}')
print(f'Média: {numsoma/cont}')
