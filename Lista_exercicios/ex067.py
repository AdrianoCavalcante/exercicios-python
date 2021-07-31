while True:
    num = int(input('Digite o número para ver sua taboada de 1 a 10 (número negativo para parar): '))
    if num < 0:
        break
    for c in range(1, 11, 1):
        print(f'{num} x {c} = {num * c}')
print('Programa encerrado!\nObrigado por usar o programa Taboada!')