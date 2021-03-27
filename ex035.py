a = float(input('Digite o comprimento da reta A do triângulo: '))
b = float(input('Digite o comprimento da reta B do triângulo: '))
c = float(input('Digite o comprimento da reta C do triângulo: '))
print('')
"""if ((b-c)**2)**(1/2) < a < (b+c):
    print('Condição 1 atendida')
    if ((a-c)**2)**(1/2) < b < (a+c):
        print('Condição 2 atendida')
        if ((a - b) ** 2) ** (1 / 2) < c < (a + b):
            print('Condição 3 atendida')
            print('')
            print('Estas retas formam um triângulo!')
else:
    print('Condições não atendidas, não é possivel formar um triângulo')"""

if a < (b+c) and b < (a+c) and c < (a + b):
    print('Estas retas formam um triângulo!')
else:
    print('Condições não atendidas, não é possivel formar um triângulo')
