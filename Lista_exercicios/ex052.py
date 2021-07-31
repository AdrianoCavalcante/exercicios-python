num = int(input('Digite um número para saber se é primo: '))
cont = 0
for c in range(1, num+1, 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if cont == 2:
    print(f'\n\033[mO NÚMERO {num} É PRIMO!')
else:
    print(f'O NÚMERO {num} NÃO É PRIMO!')

