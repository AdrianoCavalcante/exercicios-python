from time import sleep


def maior(*num):
    tot = maxi = 0
    print('-=' * 20)
    print(f'Analisando os valores passados...')
    for valor in num:
        sleep(0.5)
        print(f'{valor}', end=', ')
        tot += 1
        if tot == 1:
            maxi = valor
        else:
            if valor > maxi:
                maxi = valor
    print(f'Foram informado {tot} valores ao todo.')
    print(f'O maior valor informado foi {maxi}')


# PROGRAMA PRINCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(-1, -2)
maior(6)
maior()
