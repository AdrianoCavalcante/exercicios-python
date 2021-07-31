valores = list()
"""  Minha resolução...
cont = 0
for c in range(0, 5):
    valor = (int(input(f'Digite o {c+1}º valor: ')))
    if cont == 0:
        valores.append(valor)
        print('Primeiro valor adicionado à lista')
    else:
        if valor >= max(valores):
            valores.append(valor)
            print('Valor adicionado ao final da lista')
        elif valor <= min(valores):
            valores.insert(0, valor)
            print(f'Valor adicionado na posição {valores.index(valor)}')
        else:
            if valores[0] <= valor < valores[1]:
                valores.insert(1, valor)
                print(f'Valor adicionado na posição {valores.index(valor)}')
            elif valores[1] <= valor < valores[2]:
                valores.insert(2, valor)
                print(f'Valor adicionado na posição {valores.index(valor)}')
            elif valores[2] <= valor < valores[3]:
                valores.insert(3, valor)
                print(f'Valor adicionado na posição {valores.index(valor)}')
    cont += 1
"""

# Resolução do Guanabara:

for c in range(0, 5):
    valor = (int(input(f'Digite o {c+1}º valor: ')))
    if c == 0 or valor > max(valores):
        valores.append(valor)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {valores}')
