sexo = str(input('Digite seu sexo [ M / F ]: ')).strip().upper()[0]
while sexo not in ('M', 'F'):
    sexo = str(input('Dado inválido. Digite seu sexo [M/F]: ')).strip().upper()
print(f'Sexo: {sexo}, registrado com sucesso')
