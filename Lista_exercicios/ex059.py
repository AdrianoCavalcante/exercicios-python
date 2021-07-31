from time import sleep
menu = 0
num1 = int(input('Digite um número: '))
num2 = int(input('digite outro número: '))
while menu != 5:
    print('''Qual operação deseja realizar?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Saber qual é o maior
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa''')
    menu = int(input('Digite a opção: '))
    print('-=.' * 15)
    if menu == 1:
        print(f'A soma de {num1} com {num2} é igual a {num1+num2}')
    elif menu == 2:
        print(f'O produto de {num1} com {num2} é igual a {num1 * num2}')
    elif menu == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior é {num1}')
        else:
            print(f'Entre {num1} e {num2} o maior é {num2}')
    elif menu == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('digite outro número: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print('OPÇÃO INVÁLIDA, DIGITE NOVAMENTE A OPÇÃO!')
    print('-=.' * 15)
    sleep(2)
