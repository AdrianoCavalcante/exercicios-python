num = int(input('Digite um número: '))
num1 = float(num%2)
if num1 == 0:
    print('O numero {0} é par!'.format(num))
else:
    print('O numero {0} é impar!'.format(num))
