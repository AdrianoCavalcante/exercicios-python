n = int(input('Digite um numero inteiro para saber sua tabuada: '))
print('='*15)
for c in range(0, 10+1, 1):
    print(f'{n:5} x  {c:5} = {n*c:5}')
print('='*15)
