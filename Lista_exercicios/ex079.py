valores = list()
resp = ''
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor não adicionado, Este valor já existe na lista.')
    resp = str(input('Deseja adicionar mais um valor? [ S / N ]')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Digite apenas S para sim e N para não: ')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort()
print(f'Você digitou os valores: {valores}')
