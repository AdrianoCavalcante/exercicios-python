n = int(input('Digite um número para saber se é primo: '))
s = 0
for c in range(n, 0, -1):
    x = (n % c)
    if x == 0:
        s += 1
if s == 2:
    print('É PRIMO')
else:
    print('não')
