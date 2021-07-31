num = int(input('Fatore o número: '))
fat = 1
print(f'Calculando {num}! = ', end='')
"""while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1"""

for c in range(num, 0, -1):
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= c
    num -= 1
print(fat)
