expressao = str(input('Digite a expressão: '))
lista = list()
""" Minha resolução
for char in expressao:
    lista.append(char)
if lista.count('(') == lista.count(')'):
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está errada!')
"""
# Resolução Guanabara
for char in expressao:
    if char == '(':
        lista.append(char)
    elif char == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está errada!')
