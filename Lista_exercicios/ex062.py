termo = int(input('Digite O numero para ver suas 10 priemeiras progreções: '))
razao = int(input('Digite a razão da progreção: '))
pa = 10
conttermos = pa
while pa != 0:
    while pa != 0:
        print(termo, end=', ')
        termo += razao
        pa -= 1
    print('Pausa')
    pa = int(input('Quantos termos mais deseja ver: '))
    conttermos += pa
print(f'Você visualisou {conttermos} termos.')