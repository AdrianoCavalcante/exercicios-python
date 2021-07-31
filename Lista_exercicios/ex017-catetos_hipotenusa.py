from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é {hypot(co, ca):.2f}.')
print(f'O comprimento da hipotenusa é {((co**2)+(ca**2))**(1/2):.2f}')
