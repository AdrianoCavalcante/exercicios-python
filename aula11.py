#style: 0 para normal, 1 para negrito, 4 para sublinhado, 7 para inverter a cor da letra com a cor do fundo
#text (cor do texto): 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 magenta, 36 cyano, 37 cinza
#back (cor do fundo): 40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 magenta, 46 cyano, 47 cinza
a = 3
b = 5

print('\033[1;31;45m OLÁ MUNDO!')
print('\033[1;31;45m OLÁ MUNDO!\033[m')
print('\033[4;30;41m OLÁ MUNDO!\033[m')
print('\033[1;4;30;41m OLÁ MUNDO!\033[m')

print(f'\033[1;31;44m Os valores são {a} e {b}\033[m')
print('Os valores são {}{}{} e {}{}{}'.format('\033[4;31;44m', a, '\033[m', '\033[7;31;44m', b, '\033[m'))
