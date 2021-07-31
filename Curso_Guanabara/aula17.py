# Listas podem ser mutáveeis
# Podemos atribuir novos valore aos itens
# Podemos adicionar novos itens com os métodos lista.append('item') e
# lista.insert(posição, 'item')
# Podemos remover por indice utilizando del lista[indice] ou
# lista.pop[indice] (no método .pop se não for apontado o indice
# é considerado o ultimo item.
# Podemos remover ainda pelo conteúdo como método lista.remove('conteúdo')

# num = (2, 5, 9, 1)
# num[2] = 3
# erro... não perpitido

"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)

num.sort(reverse=True)
num.insert(2, 2)
#num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não encontrato!')
print(num)

print(f'Esta lista tem {len(num)} elementos.')"""

"""valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao final da lista')"""

a = [2, 3, 4, 7]
# b = a """Quando apresentado assim a lista "b" e a lista "a" formam uma ligação,
# se mudar um, muda o outro automatico"""
b = a[:]
"""assim cria-se uma cópia e pode mudar uma lista independente da outra"""
b[2] = 8
print(f'A lista A é {a}')
print(f'A lista B é {b}')
