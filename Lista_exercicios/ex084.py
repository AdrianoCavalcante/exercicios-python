grupo = list()
pessoa = list()
menorpeso = maiorpeso = 0
cont = 0
while True:
    resp = ''
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if cont == 0:
        menorpeso = maiorpeso = pessoa[1]
    else:
        if pessoa[1] < menorpeso:
            menorpeso = pessoa[1]
        if pessoa[1] > maiorpeso:
            maiorpeso = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    cont += 1
    while resp not in ['S', 'N']:
        resp = str(input('Quer continuar? [ S / N ]')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo foram cadastradas {cont} pessoas.')
print(f'O menor peso é {menorpeso:.2f} kg, de: ', end='')
for c, p in enumerate(grupo):
    if p[1] == menorpeso:
        print(f'{p[0]}', end=', ')
print(f'\nO maior peso é {maiorpeso:.2f} kg, de: ', end='')
for c, p in enumerate(grupo):
    if p[1] == maiorpeso:
        print(f'{p[0]}', end=', ')
