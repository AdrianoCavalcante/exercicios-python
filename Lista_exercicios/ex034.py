sal = float(input('Digite o valor do seu salário: '))
if sal > 1250.00:
    print(f'Seu aumento será de {sal*0.1:.2f}, seu salário atualizado será {sal*1.1:.2f}')
else:
    print(f'Seu aumento será de {sal*0.15:.2f}, seu salário atualizado será {sal*1.15:.2f}')
