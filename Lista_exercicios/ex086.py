matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for cl in range(0, 3):
    for cc in range(0, 3):
        matriz[cl][cc] = int(input(f'Digite um valor para {cl}, {cc}: '))
print('-=' * 30)
for cl in range(0, len(matriz)):
    for cc in range(0, len(matriz[cl])):
        print(f'[{matriz[cl][cc]:^5}]', end='')
    print()
