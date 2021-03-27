from random import randint
print('Adivinhe o número de 0 a 5 que estou pensando:')
n = int(input('Digite: '))
x = randint(0, 5)
if n == x:
    print('Parabéns você acertou')
else:
    print('Infelizmente vc não acertou! Estava pensando em {0}.'.format(x))
