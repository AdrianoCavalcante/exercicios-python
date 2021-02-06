#import math
import emoji
import random
from math import sqrt, floor, ceil
n1 = float(input('Digite um número: '))
n2 = random.random()
n3 = random.randint(1, 100)
#raiz = math.sqrt(n1:.2f)
raiz = sqrt(n1)
print(f'A raiz arredondada para baixo de {n1} é {floor(raiz)}')
print(f'A raiz exata de {n1} é {raiz:.2f}')
print(f'A raiz arredondada para cima de {n1} é {ceil(raiz)}')
print('='*50)
print(f'O número aleatório entre 0 e 1 é: {n2}')
print('='*50)
print(f'O número aleátorio entre 1 e 100 é: {n3}')
print('='*50)
print(emoji.emojize('Olá Mundo! :earth_americas:', use_aliases=True))