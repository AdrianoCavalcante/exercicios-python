numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while True:
    numuser = int(input('Digite um número entre 0 e 20: '))
    while numuser not in range(0, 21):
        numuser = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[numuser]}.')
    continuar = str(input('Deseja cotinuar? [S / N] ')).strip().upper()[0]
    if continuar == 'N':
        break
