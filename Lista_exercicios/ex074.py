from random import randint
'''num1 = randint(0, 99)
num2 = randint(0, 99)
num3 = randint(0, 99)
num4 = randint(0, 99)
num5 = randint(0, 99)
maior = menor = 0
numeros = (num1, num2, num3, num4, num5)
print(f'Os números sorteados são:{numeros}')
for cont, num in enumerate(numeros):
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')'''

#Resolução do Guanabara:
numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
for n in numeros:
    print(f'{n}', end= ', ')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
