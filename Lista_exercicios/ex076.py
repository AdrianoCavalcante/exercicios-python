lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
         'transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.3, 'Livro', 34.9)
print('=' * 32)
print('{: ^32}'.format('L I S T A   DE   P R E Ç O S'))
print('=' * 32)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<20}' + 'R$ ' + f'{lista[c+1]: >9.2f}')

# Metodo utilizado na resolução
"""for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}', end='')
    else:
        print(f'R$ {lista[c]:>9.2f}')
print('=' * 32)"""

# Outra forma de printar
#    print('{:.<20}'.format(f'{lista[c]}'), end='')
#    print('R$ ', end='')
#    print('{: >9}'.format(f'{lista[c+1]:.2f}'))
