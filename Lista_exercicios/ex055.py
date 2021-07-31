pesomaior = 0
pesomenor = 0
#usar 99999 como peso maior é gambiarra, usar a primeira leitura como referência
for c in range(1, 6, 1):
    peso = float(input(f'Qual o peso da {c}ª pessoa? '))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if pesomaior < peso:
            pesomaior = peso
        if pesomenor > peso:
            pesomenor = peso
print(f'O maior peso é: {pesomaior}')
print(f'O menor peso é: {pesomenor}')
