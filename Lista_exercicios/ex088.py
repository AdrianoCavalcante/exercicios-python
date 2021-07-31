from random import randint
from time import sleep
mega = list()
jogo = list()
cont = 0
print('-'*42)
print('{:-^42}'.format(' M E G A   S E N A '))
print('-'*42)
qtdjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print('{:-^42}'.format(' S O R T E A N D O   {}   J O G O S ').format(qtdjogos))
print()
for c in range(0, qtdjogos):
    while cont <= 5:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
    cont = 0
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
for cont, p in enumerate(mega):
    sleep(1)
    print(f'Jogo {cont+1}: {p}')
print()
print('-=' * 4+' B O A   S O R T E ! ! ! '+'-=' * 4)
