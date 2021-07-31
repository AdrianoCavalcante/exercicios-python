print('=' * 20)
print('B A N C O   C E V')
print('=' * 20)
valor = int(input('Qual valor deseja sacar? R$ '))

# Resolução com while
"""notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
while True:
    if valor >= 50:
        valor = valor - 50
        notas50 += 1
    elif valor >= 20:
        valor = valor - 20
        notas20 += 1
    elif valor >= 10:
        valor = valor - 10
        notas10 += 1
    elif valor >= 1:
        valor = valor - 1
        notas1 += 1
    if valor == 0:
        break

#Resolução com formula
notas50 = valor // 50
notas20 = (valor - (50 * notas50)) // 20
notas10 = (valor - (50 * notas50 + 20 * notas20)) // 10
notas1 = (valor - (50 * notas50 + 20 * notas20 + 10 * notas10)) // 1


if notas50 > 0:
    print(f'Total de {notas50} de R$ 50,00')
if notas20 > 0:
    print(f'Total de {notas20} de R$ 20,00')
if notas10 > 0:
    print(f'Total de {notas10} de R$ 10,00')
if notas1 > 0:
    print(f'Total de {notas1} de R$ 1,00')"""

# Resolução do Guanabara
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f' total {totced} de R$ {ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('Obrigado e volte sempre!')
