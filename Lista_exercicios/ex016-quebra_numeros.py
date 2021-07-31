from math import floor, trunc
v1 = float(input('DIGITE UM NÚMERO: '))
print(f'VOCÊ DIGITOU {v1}, A PARTE INTEIRA DESTE NÚMERO É {floor(v1)}')
print(f'VOCÊ DIGITOU {v1}, A PARTE INTEIRA DESTE NÚMERO É {trunc(v1)}')
print(f'VOCÊ DIGITOU {v1}, A PARTE INTEIRA DESTE NÚMERO É {v1//1:.0f}')
print(f'VOCÊ DIGITOU {v1}, A PARTE INTEIRA DESTE NÚMERO É {int(v1)}')