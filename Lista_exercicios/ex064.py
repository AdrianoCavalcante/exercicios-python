"""num = 0
numsoma = 0
cont = 0
while num != 999:
    num = int(input('Digite os números que deseja somar [999 para parar]: '))
    if num != 999:
        numsoma += num
        cont += 1
print(f'Você digitou {cont} números, a soma de todos é {numsoma}')"""

# Solução do Guanabara
num = int(input('Digite os números que deseja somar [999 para parar]: '))
numsoma = cont = 0
while num != 999:
    numsoma += num
    cont += 1
    num = int(input('Digite os números que deseja somar [999 para parar]: '))
print(f'Você digitou {cont} números, a soma de todos é {numsoma}')
