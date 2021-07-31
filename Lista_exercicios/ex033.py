n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))

if n1 < n2 and n1 < n3:
        print(f'O menor numero é {n1}')
if n2 < n3 and n2 < n1:
        print(f'O menor numero é {n2}')
if n3 < n1 and n3 < n2:
        print(f'O menor numero é {n3}')
if n1 > n2 and n1 > n3:
        print(f'O maior numero é {n1}')
if n2 > n1 and n2 > n3:
        print(f'O maior numero é {n2}')
if n3 > n1 and n3 > n2:
        print(f'O maior numero é {n3}')
