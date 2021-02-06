from random import randint

n = randint(0000, 9999)
n1 = str(n).zfill(4)
print(f'O número {n} possui:')
print(n1[3],' é a unidade')
print(n1[2],' é a dezena')
print(n1[1],' é a centena')
print(n1[0],' é a milhar')
print('='*30)
n = randint(0, 9999)
n1 = n//1000
n2 = n//100-n1*10
n3 = n//10-(n1*100+n2*10)
n4 = n-(n1*1000+n2*100+n3*10)
print(f'O número {n} possui:')
print(n4,' unidades')
print(n3,' dezenas')
print(n2,' centenas')
print(n1,' milhares' )
