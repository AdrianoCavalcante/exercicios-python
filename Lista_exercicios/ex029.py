vel = float(input('Velocidade: '))
ex = float(vel-80)
multa = float(ex*7)
if vel > 80:
    print('Você foi multado {:.1f}km/h acima da velocidade permitida!'.format(ex))
    print('O valor da sua multa é de: R${:.2f}'.format(multa))
