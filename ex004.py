x = input('Digite algo: ')
print('Você digitou "', (x), '".')
print('O tipo primitivo de é:', type(x))
print('"{0}" é espaço?'.format(x), x.isspace())
print('"{0}" é um numero?'.format(x), x.isnumeric())
print('"{0}" é uma letra?'.format(x), x.isalpha())
print('"{0}" é alpha numérico?'.format(x), x.isalnum())
print(f'"{x}" está tudo em maiusculo?', x.isupper())
print(f'"{x}" está tudo em minusculo?', x.islower())
print(f'"{x}" está com a primeira letra maiuscula?', x.istitle())
