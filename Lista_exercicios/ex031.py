km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
    print('Sua passagem custa R$ {0:.2f}.'.format(km*0.5))
else:
    print('Sua passagem custa R$ {0:.2f}.'.format(km*0.45))
