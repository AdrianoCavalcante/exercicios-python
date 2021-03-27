print('Vamos saber se as retas formam um triângulo: ')
l1 = float(input('Digite o comprimento da reta 1: '))
l2 = float(input('Digite o comprimento da reta 2: '))
l3 = float(input('Digite o comprimento da reta 3: '))

if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l1 + l2):
    print('Estas retas podem formar um triângulo!')
    if l1 == l2 == l3:
        print('Este triânguko é EQUILÁTERO.')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        print('Este triângulo é ISÓSCELES')
    else:
        print('este triângulo é ESCALENO.')
else:
    print('Condições não atendidas, não é possivel formar um triângulo')
