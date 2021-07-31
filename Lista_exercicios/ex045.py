from random import randint
from time import sleep
import sys
print('Vamos jogar Jokenpô?')
print(20*'-.')
print('Escolha sua opção\n1 = Pedra\n2 = Papel\n3 = Tesoura')
user = int(input('Qual sua escolha (1, 2 ou 3): '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('Pô')
print('-='*15)
if user == 1:
    print('Você escolheu Pedra')
elif user == 2:
    print('Você escolheu Papel')
elif user == 3:
    print('Você escolheu Tesoura')
else:
    print('Só pode escolher  1 para Pedra 2 para Papel e 3 para Tesoura. Tente novamente.')
    sys.exit(1)
pc = randint(1, 3)
if pc == 1:
    print('Eu escolhi Pedra')
elif pc == 2:
    print('Eu escolhi Papel')
elif pc == 3:
    print('Eu escolhi Tesoura')
if user == pc:
    print('Empate! Vanos novamente!')
elif user == 1 and pc == 2 or user == 2 and pc == 3 or user == 3 and pc == 1:
    print('Ganhei!!!')
else:
    print('Você ganhou!!!')
print('-='*15)
