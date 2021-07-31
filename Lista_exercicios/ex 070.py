total = cont = contbaratos = menorvalor = 0
maisbarato = ''
print('-=' * 20)
print('{:-^40}'.format(' LOJA SUPER BARATÃO '))
print('-=' * 20)
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Qual o valor: R$ '))
    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Deseja continuar [ S / N ]? ')).strip().upper()[0]
        if resp not in ['S', 'N']:
            print('Apenas [ S ] para Sim e [ N ] para não!')
    total += valor
    cont += 1
    if valor > 1000:
        contbaratos += 1
    if cont == 1:
        maisbarato = produto
        menorvalor = valor
    elif valor < menorvalor:
        maisbarato = produto
        menorvalor = valor
    if resp == 'N':
        break
    print('- ' * 20)
print(f'Total de gastos: R$ {total:.2f}')
print(f'Total de produtos acima de R$ 1.0000,00: {contbaratos}')
print(f'O produto mais barato foi {maisbarato} no valor de R$ {menorvalor:.2f}')
