from random import randint
print('Vamos jogar par ou impar?')
cont = 0
while True:
    user = ''
    while user not in ["P", "I"]:
        user = str(input('Você quer PAR ou IMPAR [ P / I ]? ')).strip().upper()[0]
        if user not in ["P", "I"]:
            print('Digite apenas P para PAR ou I para IMPAR!')
    numpc = randint(0, 11)
    numuser = int(input('Digite seu número: '))

    if (numpc + numuser) % 2 == 0:
        result = 'P'
    else:
        result = 'I'
    if user == result:
        print(f'O computador colocou {numpc} e o Usuário colocou {numuser}. Total {numpc + numuser},', end=' ')
        print('DEU PAR!' if result == 'P' else 'DEU IMPAR!')
        print('Você ganhou! Vamos novamente...')
        print("-=" * 20)
        cont += 1
    else:
        print(f'O computador colocou {numpc} e o Usuário colocou {numuser}. Total {numpc + numuser},', end=' ')
        print('DEU PAR!' if result == 'P' else 'DEU IMPAR!')
        print('Você perdeu!!! Parei...')
        print("-=" * 20)
        break
print(f' Você conseguiu ganhar {cont} vezes.')
