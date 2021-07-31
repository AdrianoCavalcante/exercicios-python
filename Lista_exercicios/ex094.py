grupo = list()
pessoa = {'nome': '', 'sexo': '', 'idade': 0}
resp = ''
somaidades = totpessoas = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa["sexo"] in 'M F':
            break
        print('ERRO! Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'S N':
            break
        print('ERRO! Por favor digite apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
for dados1 in grupo:
    totpessoas += 1 # poderia contar usando o len(grupo)
    for k, v in dados1.items():
        if k == 'idade':
            somaidades += v # poderia fazer a soma das idades no momento da inclusão dos dados
print(f'- O grupo tem {totpessoas} pessoas.')
mediaidade = float(somaidades/totpessoas)
print(f'- A média de idade é de {mediaidade:.2f} anos')
print('- As mulheres cadastradas foram: ', end='')
for dados2 in grupo:
    if dados2["sexo"] == 'F':
        print(dados2["nome"], end=', ')
print()
print(f'- Lista das pessoas que estão acima da média de idade:')
for dados3 in grupo:
    for k, v in dados3.items():
        if dados3["idade"] >= mediaidade:
            print(f'   {k} = {v}', end='; ')
    print()
print()
print('<<< E N C E R R A D O >>>')
