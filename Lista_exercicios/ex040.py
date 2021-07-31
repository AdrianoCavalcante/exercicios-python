n1 = float(input('Digite a sua primeira nota: '))
print(f'Sua priemira nota foi {n1:.2f}.')
print(30*'-')
n2 = float(input('Digite sua segunda nota: '))
print(f'Sua segunda nota foi {n2:.2f}.')
print(30*'-')
med = (n1+n2)/2
if med < 5.00:
    print(f'Sua média foi {med:.2f}, infelizmente está reprovado!')
elif med >= 7.00:
    print(f'Sua média foi {med:.2f}. Está aprovado! Parabens!')
else:
    print(f'Sua média foi {med:.2f}, está de recuperção! Se esforce!')
