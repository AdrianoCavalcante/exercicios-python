"""num = input('digite um número de 0 até 9999: ')
print(num)
num1 = str(num)
print('milhar: ' + num1[0])
print('centena: ' + num1[1])
print('dezena: ' + num1[2])
print('unidade: ' + num1[3])
print(num1.split())"""


#from random import randint

#n = randint(0000, 9999)
n = int(input('Digite um numero de 0 a 9999: '))
nn = str(n).zfill(4)
print(f'O número {n} possui:')
print(nn[3],' é a unidade')
print(nn[2],' é a dezena')
print(nn[1],' é a centena')
print(nn[0],' é a milhar')
print('='*30)
#n = randint(0, 9999)
n1 = n//1000
n2 = n//100-n1*10
n3 = n//10-(n1*100+n2*10)
n4 = n-(n1*1000+n2*100+n3*10)
print(f'O número {n} possui:')
print(n4,' unidades')
print(n3,' dezenas')
print(n2,' centenas')
print(n1,' milhares' )
