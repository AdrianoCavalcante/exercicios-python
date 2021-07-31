def linha():
    print('-' * 30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def soma2(*val):
    so = 0
    for nu in val:
        so += nu
    print(f'Somando os valores {val} temos {so}')


def contador(*num):
    tam = len(num)
    print(f'Recebi o valor {num}, são ao todo {tam}')
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM')
    print()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# PROGRAMA PRINCIPAL
linha()
print(f'curso em video')
linha()

titulo('CURSO EM VIDEO')
titulo('caguei')

soma(b=1, a=7)   # Podemos redefinir quem é A e quem é b
soma(2, 6)

titulo('OUTRO')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


titulo('mais um')

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)

titulo('')

soma2(2, 3, 4, 5)
