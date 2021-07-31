from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        for c in range(i, f+1, p):   # PODERIA USAR O "WHILE" NO LUGAR DO "FOR", FICARIA MAIOR O CÓDIGO
            sleep(0.5)
            print(c, end=' ')
    else:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
