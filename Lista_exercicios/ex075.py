"""num1 = int(input('Digite um número de 1 a 9: '))
while num1 not in range(1, 10):
    num1 = int(input('Favor digitar número de 1 a 9: '))
num2 = int(input('Digite outro número de 1 a 9: '))
while num2 not in range(1, 10):
    num2 = int(input('Favor digitar número de 1 a 9: '))
num3 = int(input('Digite mais um número de 1 a 9: '))
while num3 not in range(1, 10):
    num3 = int(input('Favor digitar número de 1 a 9: '))
num4 = int(input('Digite o último número de 1 a 9: '))
while num4 not in range(1, 10):
    num4 = int(input('Favor digitar número de 1 a 9: '))
conjunto = (num1, num2, num3, num4)
cont = 0
print(f'Os numeros digitados foram: {conjunto}')
print(f'O número 9 apareceu {conjunto.count(9)} vezes')
for num in conjunto:
    if num == 3:
        cont += 1
if cont == 0:
    print(f'O número 3 não apareceu em nenhuma posição')
else:
    print(f'O primeiro número 3 foi digitado na posição {conjunto.index(3) + 1}')
print('Os números pares digitados são: ', end=' ')
for num in conjunto:
    if num % 2 == 0:
        print(num, end=', ')
        cont += 1"""

# com a correção, programa melhorado
num = (int(input('Digite um número de 1 a 9: ')),
       int(input('Digite outro número de 1 a 9: ')),
       int(input('Digite mais um número de 1 a 9: ')),
       int(input('Digite o último número de 1 a 9: ')))
print(f'Os numeros digitados foram: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro número 3 foi digitado na posição {num.index(3) + 1}')
else:
    print(f'O número 3 não apareceu em nenhuma posição')
print('Os números pares digitados são: ', end=' ')
cont = 0
for n in num:
    if n % 2 == 0:
        print(n, end=', ')
        cont += 1
