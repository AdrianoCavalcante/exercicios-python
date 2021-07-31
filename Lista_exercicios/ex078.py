valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {c}: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado é {max(valores)} nas posições ', end='')
for cont, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{cont}', end=', ')
print(f'\nO menor valor digitado é {min(valores)} nas posições ', end='')
for cont, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{cont}', end=', ')