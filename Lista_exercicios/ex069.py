contmaior18 = conthomem = contmulher20 = 0
while True:
    resp = sexo = ''
    print('CADASTRO DE UMA PESSOA')
    idade = int(input('Idade: '))
    while sexo not in ['M', 'F']:
        sexo = str(input('Sexo [ M / F ]: ')).strip().upper()[0]
    if idade >= 18:
        contmaior18 += 1
    if sexo == 'M':
        conthomem += 1
    if idade <= 20 and sexo == 'F':
        contmulher20 += 1
    while resp not in ['S', 'N']:
        resp = str(input('Quer dadastrar outra pessoa, [ S ] ou [ N ]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{contmaior18} pessoas tem mais de 18 anos.')
print(f'{conthomem} cadastrados foram homens.')
print(f'{contmulher20} cadastrados são mulheres e tem menos de 20 anos.')
print('-=' * 30)
