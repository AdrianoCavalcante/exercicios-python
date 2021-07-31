from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v}')
jogo = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print('  == Ranking dos jogadores ==')
for i, v in enumerate(jogo):
    sleep(1)
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
