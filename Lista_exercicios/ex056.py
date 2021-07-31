nome = ''
sidade = 0
qtdm = 0
maioridade = 0
nomemaiori = ''
mulhermenor20 = 0
for c in range(1, 5, 1):
    sexo = ''
    print(f'Digite os dados da {c}ª pessoa:')
    nome = str(input(f'Qual o nome? ')).strip().upper()
    idade = int(input(f'Qual a idade? '))
    sidade += idade
    qtdm += 1
    while sexo not in ('M', 'm', 'F', 'f'):
        sexo = str(input(f'Qual o sexo (M / F)? ')).strip()
        if sexo not in ('M', 'm', 'F', 'f'):
            print(f'Favor entrar apenas com "M" para masculino ou "F" para feminino!')
    if sexo in 'mM' and maioridade < idade:
        maioridade = idade
        nomemaiori = nome
    if sexo in ('f', 'F') and idade < 20:
        mulhermenor20 += 1
    print('=='*20)
print(f'A média de idade do grupo é de {sidade//qtdm} anos!')
print(f'O nome do homem mais velho é: {nomemaiori}')
print(f'{mulhermenor20} mulheres têm menos de 20 anos')
