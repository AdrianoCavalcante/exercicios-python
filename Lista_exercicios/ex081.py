valores = list()
while True:
    resp = ' '
    valores.append(int(input('Digite um valor: ')))
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [ S / N ]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 NÃO faz parte da lista')
