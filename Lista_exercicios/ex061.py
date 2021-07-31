termo = int(input('Digite O numero para ver suas 10 priemeiras progreções: '))
razao = int(input('Digite a razão da progreção: '))
pa = 10
while pa != 0:
    print(termo, end=' ')
    termo += razao
    pa -= 1
