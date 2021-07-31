termos = int(input('DIGITE A QUANTIDADE DE TERMOS DA SEQUENCIA DE FIBONACCI QUE DESEJA VER: '))
cont = 0
fbn = 0
ant = 1
ant2 = 0
while termos != cont:
    cont += 1
    if cont == 1:
        fbn = 0
    elif cont == 2:
        fbn = 1
    else:
        fbn = ant + ant2
    ant2 = ant
    ant = fbn
    print(f'{fbn}', end=', ')
print('FIM!')
