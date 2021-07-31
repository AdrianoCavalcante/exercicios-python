"""tempo = int(input('Quantos anos tem o seu carro?: '))
if tempo <=3:
    print ('Carro Novo')
else:
    print ('Carro Velho')

nome = str(input('Qual o seu nome:'))
if nome == 'Adriano':
    print('lindo nome {0}'.format(nome))

else:
    print('Seu nome é bem comum {}'.format(nome))
print('Muito bom dia!')"""

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1+n2)/2
if m <=7:
    print('Sua média foi: {:.2f}, precisa melhorar!'.format(m))
else:
    print('Sua média foi: {:.2f},  parabéns!'.format(m))
