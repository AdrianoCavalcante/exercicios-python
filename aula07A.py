nome = input('Qual seu nome? ')
print('Olá {0}!'.format(nome))
print('*'*30)
n1 = float(input('{}, por favor, digite o primeiro número: '.format(nome)))
n2 = float(input('Agora digite o segundo número: '))
print('='*30)
soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
dint = n1//n2
res = n1 % n2
pot = n1**n2
print('A soma de {0} e {1} é igual a {2}'.format(n1, n2, soma))
print('a subitração de {} e {} é igual a {}'.format(n1, n2, sub))
print(f'A multiplicação entre {n1} e {n2} é igual a {mult}')
print(f'{n1} dividido por {n2} é igual a {div}')
print(f'A parte inteira de {n1} dividido por {n2} é igual a {dint}')
print(f'O resto de {n1} dividido por {n2} é igual a {res}')
print(f'{n1} elvado a potencia {n2} é igual {pot}')
