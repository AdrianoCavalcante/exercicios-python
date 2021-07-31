num = int(input('Digite um número: '))
op1 = bin(num)
op2 = oct(num)
op3 = hex(num)

tipo = int(input('Para qual base numérica deseja converter?\n1 para Binário\n2 para Octal\n3 para Hexadecimal\n'))

if tipo == 1:
    print('O número corresponde a: {0} em Binário'.format(op1))
elif tipo == 2:
    print('O número corresponde a: {0} em Octal'.format(op2))
elif tipo == 3:
    print('O número corresponde a: {0} em Hectadecimal'.format(op3))
else:
    print('Você digitou uma opção inválida')
