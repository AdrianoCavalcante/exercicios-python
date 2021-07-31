termo = int(input('Digite O numero para ver sua progreção: '))
razao = int(input('Digite a razão da progreção: '))
for c in range(termo, razao*10+termo, razao):
    print(c, end=' ')