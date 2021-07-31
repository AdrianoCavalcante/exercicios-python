from random import randint
numpc = randint(0, 10)
numuser = ''
contador = 0
print('Adivinhe o número que estou "pensando" entre 0 e 10!')
while numpc != numuser:
    numuser = int(input('Digite seu palpite: '))
    if numuser < 0 or numuser > 10:
        print('VOCÊ DIGITOU UM NÚMERO INVÁLIDO!\nDigite novamente apenas números entre 0 e 10')
    elif 0 <= numuser <= 10:
        contador += 1
    if numuser > numpc:
        print('Menos...')
    elif numuser < numpc:
        print('Mais...')
print(f'PARABÉNS!!!\nVocê acertou na {contador}ª tentativa')
