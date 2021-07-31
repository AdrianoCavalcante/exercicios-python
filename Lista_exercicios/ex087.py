matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacol3 = 0
for cl in range(0, 3):
    for cc in range(0, 3):
        matriz[cl][cc] = int(input(f'Digite um valor para {cl}, {cc}: '))
print('-=' * 30)
for cl in range(0, len(matriz)):
    for cc in range(0, len(matriz[cl])):
        print(f'[{matriz[cl][cc]:^5}]', end='')
        if matriz[cl][cc] % 2 == 0:
            somapares += matriz[cl][cc]
    print()
    somacol3 += matriz[cl][2]
print('-=' * 30)
print(f'A soma dos numeros pares é {somapares}.')
print(f'A soma dos valores da terceira coluna é {somacol3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
